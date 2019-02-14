import tweepy

file = open("seattle-freeze\keys_and_tokens.txt", "r")

keys_and_tokens = file.readlines()

x = 0
while (x < len(keys_and_tokens)):
    if "\n" in keys_and_tokens[x]:
        keys_and_tokens[x] = keys_and_tokens[x][:-1]
    x += 1

consumer_key = keys_and_tokens[0]
consumer_secret = keys_and_tokens[1]

access_token = keys_and_tokens[2]
access_token_secret = keys_and_tokens[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweet in public_tweets:
    print(tweet.text)