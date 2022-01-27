import tweepy
from datetime import date

def challengeDays():
    
    # authorization
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    # access to api
    api = tweepy.API(auth)


    start_date = date(2022, 1, 14)
    end_date = date(2022, 2, 16)
   

    # Tweeting with my dev account
    api.update_status(status = "We are currently on day " + str((days := date.today() - start_date).days) + " of 31" + " of the Kenya Twitter Bot Challenge \n"
    "Learn about how to participate here: https://dev.to/veldakiara/twitter-bot-challenge-by-kenya-twitter-developer-community-38g6 \n"
    "#BuildWhatsNext  #TwitterBotChallengeKE ")

challengeDays()


# testing 
# try:
#     api.verify_credentials()
#     print("Authentication OK")
    
# except:
#     print("Error during authentication")
