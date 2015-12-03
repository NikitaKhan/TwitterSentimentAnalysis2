#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "987657794-6WWph62qNAPDsClZcOVSx2vYs6ldzXewAKAnRCpi"
access_token_secret = "CBHlRO6QwrhOxN8EeihvGXuUKu9q8E7aYrUOqDctNCtX1"
consumer_key = "XrxmRqmrhVOhBR32OGq8lUIwS"
consumer_secret = "idVaR8ayRoJzPKFSkdZP2UOEeozsHznOKhxE4jRvRvKbYtq7bf"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        print("\n\n\n\n")
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['palestine', 'gaza', 'west bank'])


#go through and find "text:" and then just take whatever comes after that because we don't want the other stuff

