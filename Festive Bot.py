import tweepy
import random
import schedule
import time

words = ['Put your words here']

final_words = list(set(words))

# Authenticate to Twitter
auth = tweepy.OAuthHandler("API Key", "API Key Secret")
auth.set_access_token("Access Token", "Access Token Secret")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def job():
    single_tweet = random.sample(final_words, 2)
    api.update_status(status=single_tweet)
    print("Tweet Sent!")

schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
