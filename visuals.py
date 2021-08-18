"""
Suh Young Choi
CSE 163 AB

This file creates visualizations of some aggregate statistics
from the Aggregator created from the full set of TweetCongress
data. Each set of visualizations is further explained by its
own documentation.

Necessary imports:
- seaborn
- pandas
- matplotlib.pyplot
- Aggregator
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from aggs import Aggregator


DATA = "tweet_data1.csv"
ACC_VS_SPLIT = "accuracy_vs_split_data.csv"


def accuracy_vs_split(data):
    """
    Takes in data about the training percentage used in the
    PartyClassifier and corresponding accuracy scores and plots
    these in a scatter plot. Saves the image to accuracy_vs_split.png.
    """
    sns.relplot(data=data, kind='scatter',
                x='Training Percentage',
                y='Accuracy Score')

    plt.title("Accuracy Score of Models vs. Percentage Training Data")
    plt.xlabel("Training Percentage")
    plt.ylabel("Accuracy Score")

    plt.savefig('accuracy_vs_split.png', bbox_inches='tight')


def most_used_words(republicans, democrats, both):
    """
    Takes in the following parameters:
    republicans: a list of the 10 most-commonly used words and their
                 occurrences across all Republican tweets.
    democrats: a list of the 10 most-commonly used words and their
               occurrences across all Democrat tweets.
    both: a list of the 10 most-commonly used words across all
          tweets, regardless of party.

    Plots these counts as categorical plots in three images, respectively:
        - rep_top10_words.png
        - dem_top10_words.png
        - all_top10_words.png
    """
    repubs = pd.DataFrame.from_dict(republicans, orient='index',
                                    columns=['word', 'frequency'])
    dems = pd.DataFrame.from_dict(democrats, orient='index',
                                  columns=['word', 'frequency'])
    all = pd.DataFrame.from_dict(both, orient='index',
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

    sns.catplot(data=all, x='word', y='frequency')
    plt.title("Top 10 Most Frequently Used Words in All Tweets")
    plt.xlabel("Words")
    plt.ylabel("Occurrences")
    plt.savefig('all_top10_words.png')


def most_used_hashtags(republicans, democrats, both):
    """
    Takes in the following parameters:
    republicans: a list of the 10 most-commonly used hashtags and their
                 occurrences across all Republican tweets.
    democrats: a list of the 10 most-commonly used hashtags and their
               occurrences across all Democrat tweets.
    both: a list of the 10 most-commonly used hashtags across all
          tweets, regardless of party.

    Plots these counts as categorical plots in three images, respectively:
        - rep_top10_hashtags.png
        - dem_top10_hashtags.png
        - all_top10_hashtags.png
    """
    repubs = pd.DataFrame.from_dict(republicans, orient='index',
                                    columns=['hashtag', 'frequency'])
    dems = pd.DataFrame.from_dict(democrats, orient='index',
                                  columns=['hashtag', 'frequency'])
    all = pd.DataFrame.from_dict(both, orient='index',
                                 columns=['hashtag', 'frequency'])

    sns.catplot(data=repubs, x='hashtag', y='frequency')
    plt.title("Top 10 Most Frequently Used Hashtags in Republican Tweets")
    plt.xlabel("Hashtags")
    plt.ylabel("Occurrences")
    plt.savefig('rep_top10_hashtags.png')

    sns.catplot(data=dems, x='hashtag', y='frequency')
    plt.title("Top 10 Most Frequently Used Hashtags in Democrat Tweets")
    plt.xlabel("Hashtags")
    plt.ylabel("Occurrences")
    plt.savefig('dem_top10_hashtags.png')

    sns.catplot(data=all, x='hashtag', y='frequency')
    plt.title("Top 10 Most Frequently Used Hashtags in All Tweets")
    plt.xlabel("Hashtags")
    plt.ylabel("Occurrences")
    plt.savefig('all_top10_hashtags.png')


def most_used_tags(republicans, democrats, both):
    """
    Takes in the following parameters:
    republicans: a list of the 10 most-commonly used tags and their
                 occurrences across all Republican tweets.
    democrats: a list of the 10 most-commonly used tags and their
               occurrences across all Democrat tweets.
    both: a list of the 10 most-commonly used tags across all
          tweets, regardless of party.

    Plots these counts as categorical plots in three images, respectively:
        - rep_top10_tags.png
        - dem_top10_tags.png
        - all_top10_tags.png
    """
    repubs = pd.DataFrame.from_dict(republicans, orient='index',
                                    columns=['tag', 'frequency'])
    dems = pd.DataFrame.from_dict(democrats, orient='index',
                                  columns=['tag', 'frequency'])
    all = pd.DataFrame.from_dict(both, orient='index',
                                 columns=['tag', 'frequency'])

    sns.catplot(data=repubs, x='tag', y='frequency')
    plt.title("Top 10 Most Frequently Used Tags in Republican Tweets")
    plt.xlabel("Tags")
    plt.ylabel("Occurrences")
    plt.savefig('rep_top10_tags.png')

    sns.catplot(data=dems, x='tag', y='frequency')
    plt.title("Top 10 Most Frequently Used Tags in Democrat Tweets")
    plt.xlabel("Tags")
    plt.ylabel("Occurrences")
    plt.savefig('dem_top10_tags.png')

    sns.catplot(data=all, x='tag', y='frequency')
    plt.title("Top 10 Most Frequently Used Tags in All Tweets")
    plt.xlabel("Tags")
    plt.ylabel("Occurrences")
    plt.savefig('dem_top10_tags.png')


def main():
    aggs = Aggregator(DATA)

    r_hashtags = aggs.rep_hashtags
    d_hashtags = aggs.dem_hashtags
    all_hashtags = aggs.hashtags

    r_tags = aggs.rep_tags
    d_tags = aggs.dem_tags
    all_tags = aggs.tags

    r_top10_words = aggs.rep_top_ten_words
    d_top10_words = aggs.dem_top_ten_words
    all_top10_words = aggs.top_ten_words

    accuracy_vs_split(ACC_VS_SPLIT)
    most_used_words(r_top10_words, d_top10_words, all_top10_words)
    most_used_hashtags(r_hashtags, d_hashtags, all_hashtags)
    most_used_tags(r_tags, d_tags, all_tags)


if __name__ == '__main__':
    main()
