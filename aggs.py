"""
Suh Young Choi
CSE 163 AB

The Aggregator class creates an object which can compute and return
aggregate statistics about a given dataset describing the tweets of US
Representatives.

Necessary imports:
- TextBlob --> https://textblob.readthedocs.io/en/dev/install.html
- collections
"""
from textblob import TextBlob
from collections import Counter


class Aggregator:
    """
    An Aggregator contains functionality to compute and return
    different aggregate statistics about a dataset of scraped
    tweets from TweetCongress on US Representatives, such as
    the most-used words, hashtags, and tags by the Democratic
    and Republican parties. The Aggregator casts the column of
    tweets into TextBlob objects to facilitate natural language
    processing.
    """

    def __init__(self, data):
        """
        Implements an initializer for the class Aggregator. Takes
        in a CSV of data. Sets up the following:

        - separate lists for all words, hashtags, and tags that appear
          in the dataset and all words, hashtags, and tags that are used
          by both parties.
        - separate lists for the top 10 words, hashtags, and tags that
          appear in the dataset and all words, hashtags, and tags that
          are used by both parties.
        """
        data = data.dropna()
        data['text'] = data['text'].apply(TextBlob)

        self._data = data

        self._dem_words = self._get_dem_words(data)
        self._rep_words = self._get_rep_words(data)
        self._all_words = self._dem_words.join(self._rep_words)

        self._dem_hashtags, self._rep_hashtags = self._get_hashtags(data)
        self._all_hashtags = {'Democrats': self._dem_hashtags,
                              'Republicans': self._rep_hashtags}

        self._dem_tags, self._rep_tags = self._get_tags(data)
        self._all_tags = {'Democrats': self._dem_tags,
                          'Republicans': self._rep_tags}

        self._top_ten_words = self._top_tens(self._all_words)
        self._top_ten_dems_words = self._top_tens(self._dem_words)
        self._top_ten_reps_words = self._top_tens(self._rep_words)

        self._top_ten_hashtags = self._top_tens(self._all_hashtags)
        self._top_ten_dems_hashtags = self._top_tens(self._dem_hashtags)
        self._top_ten_reps_hashtags = self._top_tens(self._rep_hashtags)

        self._top_ten_tags = self._top_tens(self._all_tags)
        self._top_ten_dems_tags = self._top_tens(self._dem_tags)
        self._top_ten_reps_tags = self._top_tens(self._rep_tags)

    def _get_dem_words(self, data):
        """
        A helper function to the Aggregator class that takes in the
        given dataset and returns a list of all the words used by
        Democratic Representatives in a WordList of TextBlob objects.
        """
        dems = TextBlob("")
        dem_data = data[['party'] == 'D'][['text']]
        for tweet in dem_data:
            dems.join(tweet)
        return dems.words

    def _get_rep_words(self, data):
        """
        A helper function to the Aggregator class that takes in the
        given dataset and returns a list of all the words used by
        Republican Representatives in a WordList of TextBlob objects.
        """
        reps = TextBlob("")
        rep_data = data[['party'] == 'R'][['text']]
        for tweet in rep_data:
            reps.join(tweet)
        return reps.words

    def _get_hashtags(self, data):
        """
        A helper function to the Aggregator class that takes in the
        given dataset and returns two lists, one of Democrat-used
        hashtags and one of Republican-used hashtags.
        """
        is_rep = data['party'] == 'R'
        is_dem = data['party'] == 'D'

        rep_tweets = data[is_rep][['text']]
        dem_tweets = data[is_dem][['text']]

        rep_hashtags = set()
        dem_hashtags = set()

        for tweet in rep_tweets:
            hashtags = self.hashtags(tweet)
            rep_hashtags.update(hashtags)

        for tweet in dem_tweets:
            hashtags = self.hashtags(tweet)
            dem_hashtags.update(hashtags)

        return list(dem_hashtags), list(rep_hashtags)

    def _get_tags(self, data):
        """
        A helper function to the Aggregator class that takes in the
        given dataset and returns two lists, one of Democrat-used
        tags and one of Republican-used tags.
        """
        is_rep = data['party'] == 'R'
        is_dem = data['party'] == 'D'

        rep_tweets = data[is_rep][['text']]
        dem_tweets = data[is_dem][['text']]

        rep_tags = set()
        dem_tags = set()

        for tweet in rep_tweets:
            tags = self.tags(tweet)
            rep_tags.update(tags)

        for tweet in dem_tweets:
            tags = self.tags(tweet)
            dem_tags.update(tags)

        return list(dem_tags), list(rep_tags)

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
            freq = field.count(word)
            result[word] = freq

        return result

    def most_freq_word_per_tweet(tweet):
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

    def hashtags(tweet):
        """
        Takes in a tweet and returns the set of unique hashtags in the tweet.
        """
        hashtags = set()
        for word in tweet.words:
            if word[0] == '#':
                hashtags.add(word)
        return hashtags

    def tags(tweet):
        """
        Takes in a tweet and returns the set of unique tags in the tweet.
        """
        tags = set()
        for word in tweet.words:
            if word[0] == '@':
                tags.add(word)
        return tags

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
