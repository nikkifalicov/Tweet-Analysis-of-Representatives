# proper doc'ing tba
# flake8 pass tbd


# imports here
import pandas as pd
import re
from textblob import TextBlob
from textblob import Word
from sklearn.tree import DecisionTreeClassifier


# ALL_CAPS_CONSTANT = pd.read_csv(data.csv)
# ALL_CAPS_CONSTANT.head() to check the columns

# Tweet column to be cast as TextBlobs. 
# All functions that use 'tweet' as a parameter assume that the tweet is a TextBlob.


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



# differentiate hashtags and tag-tags
## put these in a dictionary or do a groupby?
## hashtag analysis?


# more functions, including the actual ML thing tba...
#


# main-method thing here
#   read in the data
#   put it through the ML thing
#   test out the ML thing
#   get the program to identify a random tweet - maybe some kind of test akin to assert_equals?


def main():
    pass    


if __name__ == '__main__':
    main()


# Things to go in the write-up:
#   we don't have the full tweets - could say we're focusing on the first things people see
#   runtime concerns
#   
