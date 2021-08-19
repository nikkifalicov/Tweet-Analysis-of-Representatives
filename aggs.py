"""
Suh Young Choi
CSE 163 AB

The Aggregator class creates an object which can compute and return
aggregate statistics about a given dataset describing the tweets of US
Representatives.

Necessary imports:
- collections
"""
from collections import Counter


class Aggregator:
    """
    An Aggregator contains functionality to compute and return
    different aggregate statistics about a dataset of scraped
    tweets from TweetCongress on US Representatives, such as
    the most-used words, hashtags, and tags by the Democratic
    and Republican parties.
    """

    def __init__(self, data):
        """
        Implements an initializer for the class Aggregator. Takes
        in a CSV of data. Sets up the following:

        - separate lists for all words, hashtags, and tags that appear
          in the dataset and all words, hashtags, and tags that are used
          by both parties.
        - separate lists for the top 10 words, hashtags, and tags that
          appear in the dataset and the top 10 words, hashtags, and tags
          that are used by both parties.
        """
        data['text'] = data['text'].apply(str)

        self._data = data

        self._dem_words, self._rep_words = self._get_words(data)
        self._all_words = self._dem_words + self._rep_words

        self._dem_hashtags, self._rep_hashtags = self._get_hashtags(data)
        self._all_hashtags = self._dem_hashtags + self._rep_hashtags

        self._dem_tags, self._rep_tags = self._get_tags(data)
        self._all_tags = self._dem_tags + self._rep_tags

        self._top_ten_words = self._top_tens(self._all_words)
        self._top_ten_dems_words = self._top_tens(self._dem_words)
        self._top_ten_reps_words = self._top_tens(self._rep_words)

        self._top_ten_hashtags = self._top_tens(self._all_hashtags)
        self._top_ten_dems_hashtags = self._top_tens(self._dem_hashtags)
        self._top_ten_reps_hashtags = self._top_tens(self._rep_hashtags)

        self._top_ten_tags = self._top_tens(self._all_tags)
        self._top_ten_dems_tags = self._top_tens(self._dem_tags)
        self._top_ten_reps_tags = self._top_tens(self._rep_tags)

    def _get_words(self, data):
        """
        A helper function to the Aggregator class that takes in the
        given dataset and returns two lists, one of Democrat-used
        words and one of Republican-used words. Words here include
        hashtags, tags, and other symbols.
        """
        dems = []
        is_dem = data['party'] == 'D'
        dem_data = data[is_dem]
        for tweet in dem_data['text']:
            words = tweet.split()
            dems.extend(words)

        reps = []
        is_rep = data['party'] == 'R'
        rep_data = data[is_rep]
        for tweet in rep_data['text']:
            words = tweet.split()
            reps.extend(words)

        return dems, reps

    def _get_hashtags(self, data):
        """
        A helper function to the Aggregator class that takes in the
        given dataset and returns two lists, one of Democrat-used
        hashtags and one of Republican-used hashtags.
        """
        is_rep = data['party'] == 'R'
        is_dem = data['party'] == 'D'

        rep_data = data[is_rep]
        dem_data = data[is_dem]

        rep_hashtags = []
        dem_hashtags = []

        for tweet in rep_data['text']:
            hashtags = self.hashtags(tweet)
            rep_hashtags.extend(hashtags)

        for tweet in dem_data['text']:
            hashtags = self.hashtags(tweet)
            dem_hashtags.extend(hashtags)

        return dem_hashtags, rep_hashtags

    def _get_tags(self, data):
        """
        A helper function to the Aggregator class that takes in the
        given dataset and returns two lists, one of Democrat-used tags
        and one of Republican-used tags.
        """
        is_dem = data['party'] == 'D'
        is_rep = data['party'] == 'R'

        dem_data = data[is_dem]
        rep_data = data[is_rep]

        dem_tags = []
        rep_tags = []

        for tweet in dem_data['text']:
            tags = self.tags(tweet)
            dem_tags.extend(tags)

        for tweet in rep_data['text']:
            tags = self.tags(tweet)
            rep_tags.extend(tags)

        return dem_tags, rep_tags

    def _top_tens(self, field):
        """
        A helper function to the Aggregator class that takes in a one-
        dimensional dataframe and returns the 10 most commonly-found
        objects in that dataframe. Used to find the top 10 most commonly-
        used words, tags, and hashtags across both parties.
        """
        result = {}
        top_10 = Counter(field).most_common(10)

        for word in top_10:
            result[word[0]] = word[1]

        return result

    def most_freq_word_per_tweet(self, tweet):
        """
        Takes in a tweet and returns the most frequently occurring
        word in the tweet.
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

    def hashtags(self, tweet):
        """
        Takes in a tweet and returns a list of all hashtags in the tweet.
        """
        result = []
        words = tweet.split()
        for word in words:
            if word[0] == '#':
                result.append(word)
        return result

    def tags(self, tweet):
        """
        Takes in a tweet and returns the set of all tags in the tweet.
        """
        result = []
        words = tweet.split()
        for word in words:
            if word[0] == '@':
                result.append(word)
        return result

    def data(self):
        """
        Returns the dataset used in creating the Aggregator.
        """
        return self._data

    def dem_hashtags(self):
        """
        Returns a list of all Democrat-used hashtags.
        """
        return self._dem_hashtags

    def rep_hashtags(self):
        """
        Returns a list of all Republican-used hashtags.
        """
        return self._rep_hashtags

    def all_hashtags(self):
        """
        Returns a list of all hashtags in the dataset.
        """
        return self._all_hashtags

    def dem_tags(self):
        """
        Returns a list of all Democrat-used tags.
        """
        return self._dem_tags

    def rep_tags(self):
        """
        Returns a list of all Republican-used tags.
        """
        return self._rep_tags

    def all_tags(self):
        """
        Returns a list of all tags in the dataset.
        """
        return self._all_tags

    def top_ten_words(self):
        """
        Returns a list of the top ten most commonly-used words in the
        dataset.
        """
        return self._top_ten_words

    def top_five_words(self):
        """
        Returns a list of the top five most commonly-used words in the
        dataset.
        """
        return self._top_ten_words[0:4]

    def dem_top_ten_words(self):
        """
        Returns a list of the top ten most commonly-used words in
        Democratic Representatives' tweets.
        """
        return self._top_ten_dems_words

    def dem_top_five_words(self):
        """
        Returns a list of the top five most commonly-used words in
        Democratic Representatives' tweets.
        """
        return self._top_ten_dems_words[0:4]

    def rep_top_ten_words(self):
        """
        Returns a list of the top ten most commonly-used words in
        Republican Representatives' tweets.
        """
        return self._top_ten_reps_words

    def rep_top_five_words(self):
        """
        Returns a list of the top five most commonly-used words in
        Republican Representatives' tweets.
        """
        return self._top_ten_reps_words[0:4]

    def top_ten_hashtags(self):
        """
        Returns a list of the top ten most commonly-used hashtags
        in the dataset.
        """
        return self._top_ten_hashtags

    def top_five_hashtags(self):
        """
        Returns a list of the top five most commonly-used hashtags
        in the dataset.
        """
        return self._top_ten_hashtags[0:4]

    def dem_top_ten_hashtags(self):
        """
        Returns a list of the top ten most commonly-used hashtags
        in Democratic Representatives' tweets.
        """
        return self._top_ten_dems_hashtags

    def dem_top_five_hashtags(self):
        """
        Returns a list of the top five most commonly-used hashtags
        in Democratic Representatives' tweets.
        """
        return self._top_ten_dems_hashtags[0:4]

    def rep_top_ten_hashtags(self):
        """
        Returns a list of the top ten most commonly-used hashtags
        in Republican Representatives' tweets.
        """
        return self._top_ten_reps_hashtags

    def rep_top_five_hashtags(self):
        """
        Returns a list of the top five most commonly-used hashtags
        in Republican Representatives' tweets.
        """
        return self._top_ten_reps_hashtags[0:4]

    def top_ten_tags(self):
        """
        Returns a list of the top ten most commonly-used tags in the
        dataset.
        """
        return self._top_ten_tags

    def top_five_tags(self):
        """
        Returns a list of the top five most commonly-used tags in the
        dataset.
        """
        return self._top_ten_tags[0:4]

    def dem_top_ten_tags(self):
        """
        Returns a list of the top ten most commonly-used tags in
        Democratic Representatives' tweets.
        """
        return self._top_ten_dems_tags

    def dem_top_five_tags(self):
        """
        Returns a list of the top five most commonly-used tags in
        Democratic Representatives' tweets.
        """
        return self._top_ten_dems_tags[0:4]

    def rep_top_ten_tags(self):
        """
        Returns a list of the top ten most commonly-used tags in
        Republican Representatives' tweets.
        """
        return self._top_ten_reps_tags

    def rep_top_five_tags(self):
        """
        Returns a list of the top five most commonly-used tags in
        Republican Representatives' tweets.
        """
        return self._top_ten_reps_tags[0:4]
