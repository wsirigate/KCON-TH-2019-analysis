#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1828237266-cxrlshmFdLvKhR5B9u6yB8EHG5wvgN1RTp1mCl2"
access_token_secret = "L42qX9Nwaf7IJPo0NwVaBdDhtigVCinZZmbD9n4rZNsCu"
consumer_key = "5IYlVUmQDngTYfhLRVxFHCFgf"
consumer_secret = "bMmbBWsDnHL8LSmVGvesJhdgEXqyJEu9jhkMw0GLVPHdJluvhd"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['KCON2019THAILAND', 'kcon2019thailand', 'KCON19TH', 'kcon19th', 'KCONTHAILAND2019', 'kconthailand2019'])