"""
Suh Young Choi
CSE 163 AB

Aggs: a file with functions to facilitate the computation of aggregate statistics and data insights.
"""
import re
from textblob import TextBlob
from textblob import Word


class Aggregator:

    def __init__(self):
        self._dem_hashtags = []
        self._repub_hashtags = []
        self._all_hashtags = {'Democrats' : self._dem_hashtags,
                              'Republicans' : self._repub_hashtags}
        self._dem_tags = []
        self._repub_tags = []
        self._all_tags = {'Democrats' : self._dem_tags,
                         'Republicans': self._repub_tags}
        
        # went ahead and made these top 10
        # if we want top 5, we can just select [0:4]
        self._top_ten = []
        self._top_ten_dems = []
        self._top_ten_reps = []

# functions here
    def normalize(term):
        """
        Normalizes a single word by changing it to lowercase and removing all punctuation. 
        """
        term = term.lower()
        term = re.sub(r'\W+', '', term)

        # if term[0] != '#': <-- differentiating hashtags?
        #     term = re.sub(r'\W', '', term)
        return term

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

    def top_five(tweet):
        """
        Takes in a tweet and returns the five most-occurring words in that tweet.
        """
        words = {}
        uniques = (tweet.words)
        for word in uniques:
            words[word] = tweet.words.count(word)
        sorted_words = dict(sorted(words.items(), key=lambda item: item[1]))
        return sorted_words.keys()[0:4]

    def count_hashtags(tweet):
        """
        Takes in a tweet and returns the set of unique hashtags and how many hashtags there are in the tweet.
        """
        hashtags = set()
        for word in tweet.words:
            if word[0] == '#':
                hashtags.add(word)
        return hashtags, len(hashtags)

    def count_tags(tweet):
        """
        Takes in a tweet and returns the set of unique tags and how many tags there are in the tweet.
        """
        tags = set()
        for word in tweet.words:
            if word[0] == '@':
                tags.add(word)
        return tags, len(tags)

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

# differentiate hashtags and tag-tags
## put these in a dictionary or do a groupby?
## hashtag analysis?

# Things to go in the write-up:
#   we don't have the full tweets - could say we're focusing on the first things people see
#   runtime concerns
#   
