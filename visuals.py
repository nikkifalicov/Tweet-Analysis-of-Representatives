"""
Suh Young Choi
CSE 163 AB

Visuals: a file with all the visualization methods.
"""

import math
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from aggs import Aggregator

DATA = "D:\School Stuff And Projects\UW\2021Summer\CSE 163 \
        \Final Project CSE 163\Aug 14 update\tweet_data1.csv"


# a plot for accuracy score and/or mse vs. train-test split
def accuracy_vs_split(data):
    """
    Assumes there's a two-column dataframe.
    Col1: Percentage used in training data
    Col2: Accuracy score
    """
    sns.relplot(data=data, kind='scatter', 
                x='Training Percentage',
                y='Accuracy Score')

    plt.title("Accuracy Score of Models vs. Percentage Training Data")
    plt.xlabel("Training Percentage")
    plt.ylabel("Accuracy Score")

    plt.savefig('accuracy_vs_split.png', bbox_inches='tight')


# a plot for most-used words by both parties
def most_used_words(republicans, democrats):
    """
    Both parameters will be imported in from Aggregator.
    republicans: a list of most-commonly used words and
                 how many times they occur across all R tweets.
    democrats: a list of most-commonly used words and how many
               times they occur across all D tweets.
    """
    repubs = pd.DataFrame.from_dict(republicans, orient='index',
                                    columns=['word', 'frequency'])
    dems = pd.DataFrame.from_dict(democrats, orient='index',
                                  columns=['word', 'frequency'])

    sns.catplot(data=repubs, x='word', y='frequency')
    plt.title("Top 10 Most Frequently Used Words in Republican Tweets")
    plt.xlabel("Words")
    plt.ylabel("Occurrences")
    plt.savefig('rep_top10_words.png')

    sns.catplot(data=dems, x='word', y='frequency')
    plt.title("Top 10 Most Frequently Used Words in Democrat Tweets")
    plt.xlabel("Words")
    plt.ylabel("Occurrences")
    plt.savefig('dem_top10_words.png')


# a plot for most-used hashtags in both parties
def most_used_hashtags(republicans, democrats):
    """
    Both parameters will be imported in from Aggregator.
    republicans: a list of most-commonly used hashtags
                 and how many times they occur across all R tweets.
    democrats: a list of most-commonly used hashtags and how many 
               times they occur across all D tweets.
    """
    # TBD, pass for now
    pass

def main():
    aggs = Aggregator(DATA)

    r_hashtags = aggs.repub_hashtags
    d_hashtags = aggs.dem_hashtags

    r_top10_words = aggs.repub_top_ten
    d_top10_words = aggs.dem_top_ten

    accuracy_vs_split(DATA)
    most_used_words(r_top10_words, d_top10_words)


if __name__ == '__main__':
    main()
