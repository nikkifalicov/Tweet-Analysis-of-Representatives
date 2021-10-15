"""
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


# If there are errors, replace this relative path with the absolute path of
# tweet_data.csv
DATA = 'tweet_data.csv'


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
    r_words = list(republicans.keys())
    r_freqs = list(republicans.values())
    r = {'word': r_words, 'frequency': r_freqs}
    repubs = pd.DataFrame(r)

    d_words = list(democrats.keys())
    d_freqs = list(democrats.values())
    d = {'word': d_words, 'frequency': d_freqs}
    dems = pd.DataFrame(d)

    a_words = list(both.keys())
    a_freqs = list(both.values())
    a = {'word': a_words, 'frequency': a_freqs}
    all = pd.DataFrame(a)

    sns.catplot(data=repubs, x='frequency', y='word', kind='bar',
                color='#E51F45')
    plt.title("Top 10 Most Frequently Used Words in Republican Tweets")
    plt.ylabel("Words")
    plt.xlabel("Occurrences")
    plt.savefig('rep_top10_words.png', bbox_inches='tight')

    sns.catplot(data=dems, x='frequency', y='word', kind='bar',
                color='#2B79E8')
    plt.title("Top 10 Most Frequently Used Words in Democrat Tweets")
    plt.ylabel("Words")
    plt.xlabel("Occurrences")
    plt.savefig('dem_top10_words.png', bbox_inches='tight')

    sns.catplot(data=all, x='frequency', y='word', kind='bar',
                color='#573BC4')
    plt.title("Top 10 Most Frequently Used Words in All Tweets")
    plt.ylabel("Words")
    plt.xlabel("Occurrences")
    plt.savefig('all_top10_words.png', bbox_inches='tight')


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
    r_words = list(republicans.keys())
    r_freqs = list(republicans.values())
    r = {'hashtag': r_words, 'frequency': r_freqs}
    repubs = pd.DataFrame(r)

    d_words = list(democrats.keys())
    d_freqs = list(democrats.values())
    d = {'hashtag': d_words, 'frequency': d_freqs}
    dems = pd.DataFrame(d)

    a_words = list(both.keys())
    a_freqs = list(both.values())
    a = {'hashtag': a_words, 'frequency': a_freqs}
    all = pd.DataFrame(a)

    sns.catplot(data=repubs, x='frequency', y='hashtag', kind='bar',
                color='#E51F45')
    plt.title("Top 10 Most Frequently Used Hashtags in Republican Tweets")
    plt.ylabel("Hashtags")
    plt.xlabel("Occurrences")
    plt.savefig('rep_top10_hashtags.png', bbox_inches='tight')

    sns.catplot(data=dems, x='frequency', y='hashtag', kind='bar',
                color='#2B79E8')
    plt.title("Top 10 Most Frequently Used Hashtags in Democrat Tweets")
    plt.ylabel("Hashtags")
    plt.xlabel("Occurrences")
    plt.savefig('dem_top10_hashtags.png', bbox_inches='tight')

    sns.catplot(data=all, x='frequency', y='hashtag', kind='bar',
                color='#573BC4')
    plt.title("Top 10 Most Frequently Used Hashtags in All Tweets")
    plt.ylabel("Hashtags")
    plt.xlabel("Occurrences")
    plt.savefig('all_top10_hashtags.png', bbox_inches='tight')


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
    r_words = list(republicans.keys())
    r_freqs = list(republicans.values())
    r = {'tag': r_words, 'frequency': r_freqs}
    repubs = pd.DataFrame(r)

    d_words = list(democrats.keys())
    d_freqs = list(democrats.values())
    d = {'tag': d_words, 'frequency': d_freqs}
    dems = pd.DataFrame(d)

    a_words = list(both.keys())
    a_freqs = list(both.values())
    a = {'tag': a_words, 'frequency': a_freqs}
    all = pd.DataFrame(a)

    sns.catplot(data=repubs, x='frequency', y='tag', kind='bar',
                color='#E51F45')
    plt.title("Top 10 Most Frequently Used Tags in Republican Tweets")
    plt.ylabel("Tags")
    plt.xlabel("Occurrences")
    plt.savefig('rep_top10_tags.png', bbox_inches='tight')

    sns.catplot(data=dems, x='frequency', y='tag', kind='bar',
                color='#2B79E8')
    plt.title("Top 10 Most Frequently Used Tags in Democrat Tweets")
    plt.ylabel("Tags")
    plt.xlabel("Occurrences")
    plt.savefig('dem_top10_tags.png', bbox_inches='tight')

    sns.catplot(data=all, x='frequency', y='tag', kind='bar',
                color='#573BC4')
    plt.title("Top 10 Most Frequently Used Tags in All Tweets")
    plt.ylabel("Tags")
    plt.xlabel("Occurrences")
    plt.savefig('all_top10_tags.png', bbox_inches='tight')


def words_results(republicans, democrats, both):
    """
    Prints the top 10 words used in all tweets, Democrat tweets,
    and Republican tweets; along with their frequencies.
    """
    print("Top 10 Words Across the Board:")
    print(both)
    print()
    print("Top 10 Words in Democrat Tweets:")
    print(democrats)
    print()
    print("Top 10 Words in Republican Tweets")
    print(republicans)
    print()


def hashtags_results(republicans, democrats, both):
    """
    Prints the top 10 hashtags used in all tweets, Democrat tweets,
    and Republican tweets; along with their frequencies.
    """
    print("Top 10 Hashtags Across the Board:")
    print(both)
    print()
    print("Top 10 Hashtags in Democrat Tweets:")
    print(democrats)
    print()
    print("Top 10 Hashtags in Republican Tweets")
    print(republicans)
    print()


def tags_results(republicans, democrats, both):
    """
    Prints the top 10 tags used in all tweets, Democrat tweets,
    and Republican tweets; along with their frequencies.
    """
    print("Top 10 Tags Across the Board:")
    print(both)
    print()
    print("Top 10 Tags in Democrat Tweets:")
    print(democrats)
    print()
    print("Top 10 Tags in Republican Tweets")
    print(republicans)
    print()


def main():
    aggs = Aggregator(pd.read_csv(DATA))

    r_top10_hashtags = aggs.rep_top_ten_hashtags()
    d_top10_hashtags = aggs.dem_top_ten_hashtags()
    all_top10_hashtags = aggs.top_ten_hashtags()

    r_top10_tags = aggs.rep_top_ten_tags()
    d_top10_tags = aggs.dem_top_ten_tags()
    all_top10_tags = aggs.top_ten_tags()

    r_top10_words = aggs.rep_top_ten_words()
    d_top10_words = aggs.dem_top_ten_words()
    all_top10_words = aggs.top_ten_words()

    most_used_words(r_top10_words, d_top10_words, all_top10_words)
    most_used_hashtags(r_top10_hashtags, d_top10_hashtags, all_top10_hashtags)
    most_used_tags(r_top10_tags, d_top10_tags, all_top10_tags)

    words_results(r_top10_words, d_top10_words, all_top10_words)
    hashtags_results(r_top10_hashtags, d_top10_hashtags, all_top10_hashtags)
    tags_results(r_top10_tags, d_top10_tags, all_top10_tags)


if __name__ == '__main__':
    main()
