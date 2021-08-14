"""
Suh Young Choi
CSE 163 AB

Aggs: a file with functions to facilitate the computation of aggregate statistics and data insights.
"""
import re
import pandas as pd
from textblob import TextBlob
from textblob import Word


class Aggregator:

    def __init__(self, data):
        data.astype({'text': 'TextBlob'})
        self._data = data
        self._dem_hashtags, self._repub_hashtags = self._get_hashtags(data)
        self._all_hashtags = {'Democrats' : self._dem_hashtags,
                              'Republicans' : self._repub_hashtags}
        self._dem_tags, self._repub_tags = self._get_tags(data)
        self._all_tags = {'Democrats' : self._dem_tags,
                         'Republicans': self._repub_tags}
        
        # went ahead and made these top 10
        # if we want top 5, we can just select [0:4]
        self._top_ten = []
        self._top_ten_dems = []
        self._top_ten_reps = []

# private functions (mostly for the initializer)
    def _get_hashtags(self, data):
        """
        Returns two lists, one of Democrat-used hashtags and one of Republican-used hashtags.
        """
        is_repub = data['party'] == 'R'
        is_dem = data['party'] == 'D'

        repub_tweets = data[is_repub][['text']]
        dem_tweets = data[is_dem][['text']]

        repub_hashtags = set()
        dem_hashtags = set()

        for tweet in repub_tweets:
            hashtags = count_hashtags(tweet)
            repub_hashtags.update(hashtags)
        
        for tweet in dem_tweets:
            hashtags = count_hashtags(tweet)
            dem_hashtags.update(hashtags)

        return list(dem_hashtags), list(repub_hashtags)

    def _get_tags(self, data):
        """
        Returns two lists, one of Democrat-used tags and one of Republican-used tags.
        """
        is_repub = data['party'] == 'R'
        is_dem = data['party'] == 'D'

        repub_tweets = data[is_repub][['text']]
        dem_tweets = data[is_dem][['text']]

        repub_tags = set()
        dem_tags = set()

        for tweet in repub_tweets:
            tags = count_tags(tweet)
            repub_tags.update(tags)
        
        for tweet in dem_tweets:
            tags = count_tags(tweet)
            dem_tags.update(tags)

        return list(dem_tags), list(repub_tags)

    def _top_tens(self, data):
        is_repub = data['party'] == 'R'
        is_dem = data['party'] == 'D'

        all_tweets = data[['text']]
        repub_tweets = data[is_repub][['text']]
        dem_tweets = data[is_dem][['text']]

        pd.Series(' '.join(df['text']).lower().split()).value_counts()[:100]

# functions here
    # def normalize(term):
    #     """
    #     Normalizes a single word by changing it to lowercase and removing all punctuation. 
    #     """
    #     term = term.lower()
    #     term = re.sub(r'\W+', '', term)

    #     return term

    def most_freq_word_per_tweet(tweet):
        """
        Takes in a tweet and returns the most frequently occurring word in the tweet
        """
        uniques = (tweet.words)
        highest_freq = 0
        most_freq_word = ''
        for word in uniques:
            freq = tweet.words.count(word)
            if freq > highest_freq:
                highest_freq = freq
                most_freq_word = word
        return most_freq_word

    def top_five_words_tweet(tweet):
        """
        Takes in a tweet and returns the five most-occurring words in that tweet.
        """
        words = {}
        uniques = set(tweet.words)
        for word in uniques:
            words[word] = tweet.words.count(word)
        sorted_words = dict(sorted(words.items(), key=lambda item: item[1]))
        return sorted_words.keys()[0:4]

    def count_hashtags(tweet):
        """
        Takes in a tweet and returns the set of unique hashtags in the tweet.
        """
        hashtags = set()
        for word in tweet.words:
            if word[0] == '#':
                hashtags.add(word)
        return hashtags

    def count_tags(tweet):
        """
        Takes in a tweet and returns the set of unique tags in the tweet.
        """
        tags = set()
        for word in tweet.words:
            if word[0] == '@':
                tags.add(word)
        return tags

# display functions:
    def dem_hashtags(self):
        return self._dem_hashtags

    def repub_hashtags(self):
        return self._repub_hashtags

    def hashtags(self):
        return self._all_hashtags
    
    def dem_tags(self):
        return self._dem_tags

    def repub_tags(self):
        return self._repub_tags
    
    def tags(self):
        return self._all_tags

    def top_ten_words(self):
        return self._top_ten
    
    def top_five_words(self):
        return self._top_ten[0:4]

    def dem_top_ten(self):
        return self._top_ten_dems

    def dem_top_five(self):
        return self._top_ten_dems[0:4]
    
    def repub_top_ten(self):
        return self._top_ten_repubs

    def repub_top_five(self):
        return self._top_ten_repubs[0:4]
