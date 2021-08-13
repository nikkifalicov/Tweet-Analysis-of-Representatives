from PartyClassifier import PartyClassifier
import pandas as pd

def main():
    test_csv = pd.read_csv('tweet_test')
    test = PartyClassifier(test_csv)
    test.add_tweet_polarity()
    # print(test.get_column_names())
    # print(test.fit_and_predict_party())
    # print(test._model_with_names())
    # print(test._compare_outcomes())
    

    