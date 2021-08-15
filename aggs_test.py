"""
Suh Young Choi
CSE 163 AB

aggs_test: a tester file for the functions in the Aggregator class
"""

from aggs import Aggregator
# from cse163_utils import assert_equals

DATA = '/home/test.csv'


def test_display_functions(agg):
    print("Democrat hashtags: " + str(agg.dem_hashtags))
    print("Republican hashtags: " + str(agg.repub_hashtags))
    print("All hashtags: " + str(agg.hashtags))

    print()

    print("Democrat tags: " + str(agg.dem_tags))
    print("Republican tags: " + str(agg.repub_tags))
    print("All tags: " + str(agg.tags))

    print()

    print("Top ten words across the board: " + str(agg.top_ten_words))
    print("Top five words across the board: " + str(agg.top_five_words))

    print()

    print("Top ten Democratic words: " + str(agg.dem_top_ten))
    print("Top five Democratic words: " + str(agg.dem_top_five))

    print()

    print("Top ten Republican words: " + str(agg.repub_top_ten))
    print("Top five Republican words: " + str(agg.repub_top_five))

    print()
    print("Display functions complete.")


def main():
    agg = Aggregator(DATA)
    print("Aggregator successfully initialized.")
    test_display_functions(agg)


if __name__ == '__main__':
    main()