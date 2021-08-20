"""
Suh Young Choi
CSE 163 AB

This file allows a user to view the functions which will be
later used in visuals.py, and to check that their output is
correct. This file uses a scaled-down version of the full
TweetCongress dataset for testing purposes.

Necessary imports:
- Aggregator
"""
from aggs import Aggregator
import pandas as pd
import os

# If error, replace with absolute path to tweet_data2
DATA = 'tweet_data2'


def test_hashtag_functions(agg):
    """
    Prints all fields from the Aggregator class relating to hashtags
    """
    print("Democrat hashtags:")
    print(agg.dem_hashtags())
    print()
    print("Republican hashtags:")
    print(agg.rep_hashtags())
    print()
    print("All hashtags:")
    print(agg.all_hashtags())
    print()
    print("Top 10 Hashtags Across the Board:")
    print(agg.top_ten_hashtags())
    print()
    print("Top 10 Democrat hashtags:")
    print(agg.dem_top_ten_hashtags())
    print()
    print("Top 10 Republican hashtags:")
    print(agg.rep_top_ten_hashtags())


def test_tag_functions(agg):
    """
    Prints all fields from the Aggregator class relating to tags.
    """
    print("Democrat tags:")
    print(agg.dem_tags())
    print()
    print("Republican tags:")
    print(agg.rep_tags())
    print()
    print("All tags:")
    print(agg.all_tags())
    print()
    print("Top 10 Tags Across the Board:")
    print(agg.top_ten_tags())
    print()
    print("Top 10 Democrat tags:")
    print(agg.dem_top_ten_tags())
    print()
    print("Top 10 Republican tags:")
    print(agg.rep_top_ten_tags())


def test_top10s_functions(agg):
    """
    Prints all fields from the Aggregator class relating to words.
    """
    print("Top ten words across the board:")
    print(agg.top_ten_words())
    print()
    print("Top ten Democratic words:")
    print(agg.dem_top_ten_words())
    print()
    print("Top ten Republican words: ")
    print(agg.rep_top_ten_words())


def main():
    agg = Aggregator(pd.read_csv(DATA))
    print("Aggregator successfully initialized.")
    print()

    test_hashtag_functions(agg)
    print("***HASHTAG TESTING COMPLETE***")
    print()

    test_tag_functions(agg)
    print("***TAG TESTING COMPLETE***")
    print()

    test_top10s_functions(agg)
    print("***TOP 10S TESTING COMPLETE***")
    print()
    print()
    print("You're good to go!")


if __name__ == '__main__':
    main()
