#!/usr/bin/python3

from re import sub
import sys
import json
import creds
import tweepy     # https://github.com/tweepy/tweepy
import markovify  # https://github.com/jsvine/markovify

CONSUMER_KEY = creds.consumer
CONSUMER_SECRET_KEY = creds.consumer_secret
ACCESS_KEY = creds.access
ACCESS_SECRET_KEY = creds.access_secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET_KEY)
api = tweepy.API(auth)

def get_tweets(screen_name):
	"""
	Downloads a user's tweets. Twitter API only lets us get the last 3200 or so.
	"""
	tweet_list = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name, count=200 , tweet_mode="extended").items():
		tweet = sub(r"http\S+", "", tweet.full_text) # Trim URLS, grab full text
		tweet_list.append(tweet)
		print("Downloaded " + str(len(tweet_list)) + " tweets so far.", end='\r')
	print()
	return tweet_list


def markovify_tweets(corpus):
	"""
	Markovifies the corpus using a state size of 3 and returns
	the text model.
	"""
	with open(corpus) as f:
		text = f.read()
		text_model = markovify.Text(text, state_size=3)
	return text_model


def usage():
	"""
	Prints usage information.
	"""
	print("Usage: {} [username]".format(sys.argv[0]))
	print("[username] must be a valid Twitter username.")
	sys.exit(1)


def main():
	try:
		user = api.get_user(sys.argv[1])
		num_tweets = api.get_user(sys.argv[1]).statuses_count
		print("Found user {} with {} tweets.".format(sys.argv[1], num_tweets))
		if num_tweets > 3200:
			print("We can only download the last 3200 of these.")
	except tweepy.TweepError as e:
		print(e.args[0][0]['message'])
		usage()
	inp = input("Continue? (y/n) ")
	if inp == ('y' or 'Y'):
		tweets = get_tweets(sys.argv[1])
		user_corpus = "{}_corpus.txt".format(sys.argv[1])
		with open(user_corpus, 'a') as f:
			for i in range(len(tweets)):
				f.write(tweets[i])
		model = markovify_tweets(user_corpus)
		print("Exporting model...")
		with open("{}_model.json".format(sys.argv[1]), 'w') as f:
			model_json = model.to_json()
			json.dump(model_json, f)
		print('Done.')
	else:
		pass


if __name__ == '__main__':
	if len(sys.argv) != 2:
		usage()
	main()	
