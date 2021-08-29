
# GetTweets

GetTweets is an Automation Tool Written in Python to Fetch Tweets that have a particular Hashtag or word and then directly upload it to Your GitHub Repository.
It can be used in many ways to Automate your Notekeeping or Reconnaissance Process.

![enter image description here](https://user-images.githubusercontent.com/29165227/131255538-1437b7fe-f9f0-4bdb-b05b-8a7c974252b5.png)

## Usage
`python3 ./GetTweets.py`

![enter image description here](https://user-images.githubusercontent.com/29165227/131255854-b6297f42-62fb-4a67-8615-1e6c1af14210.png)
## Installation
- ` git clone https://github.com/MayankPandey01/GetTweets.git`
- After Installation Setup the `config.py` file using Your Tokens From Twitter Developer Account and Github

## Recommended Python Version:
This Tool Only Supports Python 3.
The recommended version for Python 3 is 3.8.x.

## Dependencies:

The dependencies can be installed using the requirements file:

Installation on Windows:
- python.exe -m pip3 install -r requirements.txt.

Installation on Linux.
- sudo pip3 install -r requirements.txt.

## How this Works

This Program Interacts with Twitter API using the tweepy module, it is used to fetch the tweets from the Mentioned user in the `config.py` file, and then the Github API is used to upload the file to your Repository.
 
 > Config.py

This file contains all the Configuration Needed to Run the Program. You will need the following things to set up the Configuration File

- Twitter Developer Account to access the Twitter API. You Can Apply for one here https://developer.twitter.com/en/apply-for-access
- A Github Developer Access Token. Get Yours From Here https://github.com/settings/tokens


> db.json

This File is used to create a local database that keeps a record of the most recent tweet of the User who has been Queried using the Program.
This helps to keep the Result Free from Duplication and always give new Results.
