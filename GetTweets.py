try:
	import tweepy
	from github import Github
	import sys
	import colorama
	import json
	from config import *
	
	
except ModuleNotFoundError as e:
	print ("\nModule Error: ",e)
	print ("")
	sys.exit(0)


except ImportError as e:
	print ("\nImport Error: ",e)
	print ("")
	sys.exit(0)

colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
RED = colorama.Fore.RED
BLUE = colorama.Fore.BLUE
CYAN = colorama.Fore.CYAN


def check_db(screen_name):
	print(f"{GREEN}\n[*] Checking Database For Previous Entries For{RESET}", screen_name, f"{GREEN} Tweets\n")
	with open('db.json') as json_file:
		data = json.load(json_file)
		for i in range(len(data["fetchedResults"])):
			if screen_name in data["fetchedResults"][i].keys():
				print(f"{GREEN}[*] ENTRY FOUND. FETCHING MOST RECENT TWEETS\n")
				since_id=data["fetchedResults"][i].get(screen_name)
				return True,since_id
			else:
				pass
		print(f"{RED}[*] NO ENTRY FOUND\n")
		return False,0

def update_db(screen_name,since_id):
	try:
		print(f"{GREEN}[*] UPDATING DATABASE\n")
		with open('db.json','r+') as json_file:
			p=screen_name
			q=since_id
			file_data = json.load(json_file)
			new_data={p:q}
			file_data["fetchedResults"].append(new_data)
			json_file.seek(0)
			json.dump(file_data, json_file, indent = 4)
		print(f"{GREEN}[*] DATABASE UPDATED\n")
	except:
		print(f"{RED}[*] AN ERROR OCCURED WHILE UPDATING DATABASE\n")
		sys.exit()






def banner():

	ascii_banner=rf"""{RED}

	
   _____      _   _______                _       
  / ____|    | | |__   __|              | |      
 | |  __  ___| |_   | |_      _____  ___| |_ ___ 
 | | |_ |/ _ \ __|  | \ \ /\ / / _ \/ _ \ __/ __|
 | |__| |  __/ |_   | |\ V  V /  __/  __/ |_\__ \
  \_____|\___|\__|  |_| \_/\_/ \___|\___|\__|___/
                                               
                                                
                                                                                                

	"""
	
	print(ascii_banner)


def main():

	print(f"{GREEN}[*] Authenticating with Twitter...{RESET}")
	print("")
	try:
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
		api = tweepy.API(auth)
		authenticated_user=api.me()
		authenticated_user_name=authenticated_user.screen_name
		tweets_string=[]
		test_tweets_string=[]
		
		print(f"{GREEN}[*] User Authenticated{RESET} -->" ,authenticated_user_name)
	except:
		print(f"{RED}[!] An Error Occurred While Authentication On Twitter{RESET}")
		print("")
		sys.exit()
	print("")
	print("")
	print(f"{RED}[#] Searching Tweets of {RESET}" ,screen_name, f"{RED}for{RESET}", search_term)
	print("")
	
	x,y=check_db(screen_name)
	if x:
		since_id=y
		try:
			tweets = api.user_timeline(screen_name,count=500,since_id=since_id,include_rts = include_re_tweets,tweet_mode ='extended')
		except:
			print(f"{RED}[!] An Error Occurred While Fetching Tweets{RESET}\n\n")
			sys.exit()

	else:
		try:
			tweets = api.user_timeline(screen_name,count=500,include_rts = include_re_tweets,tweet_mode ='extended')
		except:
			print(f"{RED}[!] An Error Occurred While Fetching Tweets{RESET}\n\n")
			sys.exit()


	
	
	retrived_tweets=0
	for i in range(0,len(tweets)):
			most_recent_since_id = tweets[0].id_str
			p=tweets[i]
			if  search_term in p.full_text and p.author.screen_name ==screen_name:
				tweets_string.append('- ')
				tweets_string.append(p.full_text)
				tweets_string.append('\n')
				tweets_string.append('\n')
				tweets_string.append('\n')
				retrived_tweets+=1                    
	print('')
	if retrived_tweets!=0:
		print(f"{GRAY}[*] Total Tweets Found -->{RESET}{RED}" ,retrived_tweets)
	else:
		print(f"{RED}[!] No Recent Tweets Found For Given User and Search Term{RESET}\n\n")
		print(f"{RED}\n[!] Quitting!! \n") 
		sys.exit()

	print('')
	file1 = open(filename, 'a' , encoding="utf-8")
	print(f"{RESET}{CYAN}[*] Creating File...")
	print('')
	try:
		file1.writelines(tweets_string)
	except:
		print("")
		print(f"{RED}[!] Unicode Error Occurred , You have a Emoticon that can not be rendered{RESET} ") 
		print('')
	finally:
		file1.close()
		print(f"{CYAN}[*] File Created :",filename)
		print('')

	print('')
	print(f"{GREEN}[*] Authenticating with GitHub...{RESET}")
	print('')

	try:
		g = Github(GITHUB_TOKEN)
		user=g.get_user()
		print(f"{GREEN}[*] User Authenticated -->{RESET}" ,user.login)
	except :
		print(f"{RED}[!] An Error Occurred While Authentication On GitHub{RESET}\n\n")
		sys.exit()
	
	
	print('')
	
	repo = g.get_user().get_repo(repo_name) 
	all_files = []
	contents = repo.get_contents("")
	while contents:
	
	    file_content = contents.pop(0)
	    if file_content.type == "dir":
	        pass
	    else:
	        file = file_content
	        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
	with open(filename, 'r', encoding="utf-8") as file:
	   try:
	   	content = file.read()
	   except:
	    print("")
	    print(f"{RED}[!] Unicode Error Occurred , You have a Emoticon that can not be rendered{RESET} ") 
	    print('')
	    sys.exit()
	print('')
	print('')
	print(f"{CYAN}[*] Uploading File to GitHub")
	print('')
	print(f"[*] Uploading to Repository --> {RESET}", repo_name)
	print('')
	print('')
	git_file = git_prefix + filename 
	if git_file in all_files:
	    contents = repo.get_contents(git_file)
	    repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
	    print(git_file + f"  {RED}[*] Already exists. Updating It..{RESET}")
	    print('')
	    print(git_file + f'  {GREEN}[*] UPDATED')
	    print('')
	else:
	    repo.create_file(git_file, "committing files", content, branch="main")
	    print('')
	    print(git_file + f'  {GREEN}[*] UPLOADED')
	    print('')
	print('')

	update_db(screen_name,most_recent_since_id)



if __name__ == "__main__":
	try:
		banner()	
		main()

	except KeyboardInterrupt:
		print("")
		print (f"{RED} Keyboard Interrupt Detected {RESET}\n")
		sys.exit(0)

