# proper doc'ing tba
# flake8 pass tbd

# testing here! -Nikki

# imports here
#   scraper tba?
#   scikitlearn?
import pandas as pd
import re
from textblob import TextBlob
from textblob import Word
from sklearn.tree import DecisionTreeClassifier


# ALL_CAPS_CONSTANT = pd.read_csv(data.csv)
# ALL_CAPS_CONSTANT.head() to check the columns

# cast the tweet column into TextBlobs


# functions here
def normalize(term):
    term = term.lower()
    term = re.sub(r'\W+', '', term)

    # if term[0] != '#': <-- differentiating hashtags?
    #     term = re.sub(r'\W', '', term)
    return term


def most_freq_word_per_tweet(tweet):
    # consider stopwords?
    uniques = (tweet.words)
    highest_freq = 0
    most_freq_word = ''
    for word in uniques:
        freq = tweet.words.count(word)
        if freq > highest_freq:
            highest_freq = freq
            most_freq_word = word
    return most_freq_word


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
