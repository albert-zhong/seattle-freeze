from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import os
import csv
import codes
import locations

class csv_listener(StreamListener):

    def on_status(self, status):
        with open("/home/albert/workspace/seattle-freeze/data/seattle.csv", "a") as f:
            writer = csv.writer(f)
            sanitized_text = ignore_non_ascii(status.text)
            blob = TextBlob(sanitized_text)
            writer.writerow([status.author.screen_name, status.created_at, sanitized_text, blob.polarity, blob.subjectivity])
            print("Row added")

    def on_error(self, status):
        print(status)
        return False

    def on_timeout(self):
        print (sys.stderr, 'Timeout...')
        return False # kill the stream

def ignore_non_ascii(text):
    return str(text.encode('utf-8').decode('ascii', 'ignore'))

def write_to_csv(location, path):
    # Writing csv titles if csv file is empty
    if os.stat(path).st_size == 0:
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Author', 'Date', 'Text', 'Polairty', 'Subjectivity'])

    # Create Twitter stream
    auth = OAuthHandler(codes.ckey, codes.csecret)
    auth.set_access_token(codes.atoken, codes.asecret)

    twitterStream = Stream(auth, csv_listener())
    twitterStream.filter(locations=location)
