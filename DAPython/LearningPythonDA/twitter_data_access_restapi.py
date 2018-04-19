# This program prints all tweets from a certain user.

import json
from tweepy import OAuthHandler, API

consumer_key = "pfmIDDr4ETfgBtCbJ5WDg6UJZ"
consumer_key_secret = "k2t1sCHakqdDpGcnFOXXJxN5h0vJ3iKZIzfnDlZKph4ozpylNA"
access_token = "900770662268018688-iRRPscUd5pZcHmVeddbFoAlshZ25noh"
access_token_secret = "sxT6rzAjNrNmILUyovq8uceyE9jPYlXnQflt9XttQ8xnK"

# Authenticating with the Twitter API
auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)


# Gets the tweets for a particular user handle.
def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200) # Shows 200 most recent tweets
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


# Ensuring the program is meant to be run as a script

if __name__ == '__main__' :
    pull_down_tweets(auth.username) # Shows the tweets for whichever user is currently logged in.