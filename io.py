import tweepy
import os
import pandas as pd
consumer_key = "os.environ.get('consumer_key')"
consumer_secret = "os.environ.get('consumer_secret')"
access_token = "os.environ.get('access_token')"
access_token_secret = "os.environ.get('access_token_secret')"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# create list to append tweets to
tweets = []

# append all tweet data to list
for tweet in tweepy.Cursor(api.search,q='#BigFourAgenda OR #bigfouragenda OR Big Four Agenda',count=10000000,
                       until="2019-03-20").items(10000000):
    tweets.append(tweet)

# convert 'tweets' list to pandas.DataFrame
tweets_df = pd.DataFrame(vars(tweets[i]) for i in range(len(tweets)))

# define file path (string) to save csv file to
FILE_PATH = 'io2.txt'

# use pandas to save dataframe to csv
tweets_df.to_csv(FILE_PATH)
