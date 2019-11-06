import tweepy  # https://github.com/tweepy/tweepy
import csv
import json


class TwitterClient(object):
  def __init__(self, consumer_key, consumer_secret, access_key, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    self.api = tweepy.API(auth)

  def search_for(self, search_term):
    new_tweets = self.api.search(
        search_term, tweet_mode="extended", trim_user=True, count=200)
    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before " + str(oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = self.api.search(
          search_term, tweet_mode="extended", trim_user=True, count=200,max_id = oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("tweets downloaded so far: " + str(len(alltweets)))

    with open('{}.json'.format(search_term.replace(" ", "_")), 'w', encoding='utf-8') as f:
      json.dump([status._json for status in alltweets],
                      f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
	CONSUMER_KEY = "ck"  # (API key)
	# (API secret key)
	CONSUMER_SECRET = "cs"

	# (Access token)
	ACCESS_TOKEN = "at"
	# (Access token secret)"
	ACCESS_SECRET = "as"
	search_terms = ["ThredUp", "RealReal",
                 "VestaireCollective", "online resale fashion", "secondhand clothes", "secondhand design"]
	twitter_client = TwitterClient(
            CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
	for search_term in search_terms:
	  twitter_client.search_for(search_term)
