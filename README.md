<h2>Overview</h2>

lyrebird uses tweepy and markovify to build a markov model of a given twitter user. It generates tweets based on that user's writing style and vocabulary.

To use, install the libaries in requirements.txt and enter your Twitter API credentials in creds.py. Then you can generate a model of a user with build_model.py and generate imitation tweets with generate.py.

This is sort of a prototype I wanted to throw together to see if it worked. Needs some adjustment to create more coherent tweets.

<h2>Usage</h2>

```
$ ./build_model.py realDonaldTrump
Found user realDonaldTrump with 47148 tweets.
We can only download the last 3200 of these.
Continue? (y/n) y
Downloaded 3196 tweets so far.
Exporting model...
Done.
```

```
$ ./generate.py realDonaldTrump_model.json 5
Importing model...
Generating tweets...

The Impeachment Hoax is such a bad precedent and sooo bad for our Country!Impeachment Witch Hunt is now OVER!

“What has happened here with the Anthony Wiener laptop, the Server, all of the Fake News wants to talk about Ukraine.

Vote for Tate on Tuesday!…RT @realDonaldTrump: Big Rally in Minneapolis.....the area and start a new war all over again.

California desperately needs water, and you can add to that many votes from voters that don’t talk about their experience at the Black Voices For Trump event along with the reputations of many pundits.

They should, a perfect call - got them by surprise!“The Democrats have been engaged in a three-year-long impeachment parade in search of a rationale.
```
