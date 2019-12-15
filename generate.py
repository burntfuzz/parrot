#!/usr/bin/python3

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

def import_model(model_file):
	print("Importing model...")
	try:
		with open(model_file, 'r') as f:
			model = json.load(f)
		return markovify.Text.from_json(model)
	except (FileNotFoundError, IOError) as e:
		print(e)
		usage()


def usage():
	"""
	Prints usage information.
	"""
	print("Usage: {} [corpus_json_file] [count]".format(sys.argv[0]))
	print("[corpus_json_file] is the json model file generated from build_model.py")
	print("[count] is the number of imitation tweets to generate.")
	sys.exit(1)


def main():
	tweet_choices = []
	model = import_model(sys.argv[1])
	print("Generating tweets..." + '\n')
	for i in range(int(sys.argv[2])):
		tweet = model.make_short_sentence(280, min_chars=70, tries=20)
		print(tweet + '\n')
		tweet_choices.append(tweet)


if __name__ == "__main__":
	if len(sys.argv) != 3:
		usage()
	main()