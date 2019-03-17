from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob

import os
import csv

import codes


class GeoListener(StreamListener):

    def __init__(self, path, api=None):
        super().__init__(api=None)
        self.path = path
        self.counter = 0

    def on_status(self, status):
        with open(self.path, "a") as f:
            writer = csv.writer(f)
            sanitized_text = ignore_non_ascii(status.text)  # Ignores non-ASCII text for TextBlob compatibility
            blob = TextBlob(sanitized_text)
            writer.writerow([status.author.screen_name, status.created_at, sanitized_text, blob.polarity, blob.subjectivity])

            #  Prints row count to console
            self.counter += 1
            print("row " + str(self.counter) + " added")

    def on_error(self, status_code):
        print(status_code)
        return False  # kill the stream

    def on_timeout(self):
        print('Timeout...')
        return False  # kill the stream


def ignore_non_ascii(text):
    return str(text.encode('utf-8').decode('ascii', 'ignore'))


def create_stream(location):

    # Create path
    path = get_path(location[1])  # location[0] are coordinates, location[1] is location name string

    # Create CSV file if it doesn't exist already
    if os.path.isfile(path) is False:
        with open(path, 'w+') as f:
            writer = csv.writer(f)
            writer.writerow(['Author', 'Date', 'Text', 'Polarity', 'Subjectivity'])

    # Create Twitter stream
    auth = OAuthHandler(codes.consumer_key, codes.consumer_secret)
    auth.set_access_token(codes.access_token, codes.access_secret)

    # Create StreamListener
    csv_listener = GeoListener(path)
    my_stream = Stream(auth, csv_listener)

    my_stream.filter(locations=location[0])  # location[0] are coordinates, location[1] is location name string


def get_path(name):  # Creates path for CSV file based on location
    here = os.path.dirname(os.path.realpath(__file__))
    file_name = name + ".csv"
    data_folder_path = "data"
    file_path = os.path.join(here, os.pardir, data_folder_path, file_name)
    return file_path
