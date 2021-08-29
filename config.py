#Add you Twitter Developer Account Tokens Here

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

#Add you GitHub Personal Access Tokens

GITHUB_TOKEN = ''


screen_name ='mayank_pandey01'  # Twitter Username Whose tweet You want to Fetch
search_term= '#bugbounty'       # The Search Term    

filename=screen_name+".md"      # File Extension , (.md works the best)

include_re_tweets=True          # Tells the Program To include the Re-Tweets by the User


git_prefix = 'output/'       # The folder you want to upload , leave it empty if you don't want to upload it in a folder
repo_name='GetTweets'        # Add your repo where you want to upload the file