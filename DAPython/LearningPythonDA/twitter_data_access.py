# This program prints incoming tweets from the twitter data stream!

from tweepy import OAuthHandler, Stream
from tweepy import StreamListener

consumer_key = "pfmIDDr4ETfgBtCbJ5WDg6UJZ"
consumer_key_secret = "k2t1sCHakqdDpGcnFOXXJxN5h0vJ3iKZIzfnDlZKph4ozpylNA"
access_token = "900770662268018688-iRRPscUd5pZcHmVeddbFoAlshZ25noh"
access_token_secret = "sxT6rzAjNrNmILUyovq8uceyE9jPYlXnQflt9XttQ8xnK"

# Authenticating with the Twitter API
auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)


# Creating the Stream Handler
class PrintListener(StreamListener):
    #Overriding the on_status method
    def on_status(self, status):
        print(status.text)
        print(status.author.screen_name,
              status.created_at,
              status.source,
              "\n")

    def on_error(self, status_code):
        print("Error Code: {} ".format(status_code))
        return True # Keeps the stream alive

    def on_timeout(self):
        print("Listener timed out!")
        return True # Keeps the stream alive


# Accessing the Twitter Data stream
def print_to_terminal():
    listener = PrintListener()
    stream  = Stream(auth, listener)
    stream.sample()


# Ensuring the program is meant to be run as a script

if __name__ == '__main__' :
    print_to_terminal()