<h2>Overview</h2>
parrot uses tweepy and markovify to build a markov model of a given twitter user. It generates tweets based on that user's writing style and vocabulary.

To use, install the libaries in requirements.txt and enter your Twitter API credentials in creds.py. Then you can generate a model of a user with build_model.py and generate imitation tweets with generate.py.

I threw this together to experiment with markov chains and the Twitter API. Needs some adjustment to create more coherent tweets.

<h2>Requirements</h2>

Install the required modules with `pip install -r requirements.txt`.

 - `tweepy`
 - `markovify`
 
You'll also need a valid Twitter API credentials.

<h2>Usage</h2>

```
$ ./build_model.py realTwitterUser
Found user realTwitterUser with 47148 tweets.
We can only download the last 3200 of these.
Continue? (y/n) y
Downloaded 3196 tweets so far.
Exporting model...
Done.
```

```
$ ./generate.py realTwitterUser_model.json 5
Importing model...
Generating tweets...

[...]

```
