import json
import re

search_terms = ["ThredUp", "RealReal",
                "VestaireCollective", "online resale fashion", "secondhand clothes", "secondhand design", "secondhand fashion"]


def get_text(tweets):
    return [re.sub(r"http\S+", "", get_tweet_text(x)) for x in tweets]


def get_tweet_text(tweet):
    if 'full_text' in tweet:
        return tweet['full_text']
    else:
        return tweet['text']

for search_term in search_terms:
  json_file = '{}.json'.format(search_term.replace(" ", "_"))
  txt_file = '{}.txt'.format(search_term.replace(" ", "_"))
  with open(json_file, 'r') as f:
    tweets = json.load(f)

  text_tweets_ary_1 = get_text(tweets)
  # text_tweets_ary = [re.sub('RT @[\w_]+: ', '', x) for x in text_tweets_ary_1]
  text_tweets = "\n".join([x.rstrip() for x in text_tweets_ary_1 if x.strip(
  ) and len(x) > 10]).replace("\n\n", "\n")

  with open(txt_file, 'w', encoding='utf-8') as f:
      # json.dump(text_tweets,
      # 					f, ensure_ascii=False, indent=4)
          f.write(text_tweets)
