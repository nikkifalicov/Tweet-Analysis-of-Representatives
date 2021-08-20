"""
Nikki Falicov
CSE 163 AB
This class contains code to test and view results from the machine
learning model in PartyClassifier.py

necessary imports:
    - pandas
    - PartyClassifier
    - os
"""
from party_classifier import PartyClassifier
import pandas as pd
import os


def tweet_test_set():
    """
    tweet_test_set() prints results from the machine learning
    model trained on the 'tweet_test' csv file
    """
    test_csv = pd.read_csv('tweet_test')
    test = PartyClassifier(test_csv)
    print(test.get_column_names())
    train_acc, test_acc = test.fit_and_predict_party()
    results(test, train_acc, test_acc)


def tweet_data1_test(data):
    """
    tweet_data1(data) prints results from the machine learning
    model trained on the 'tweet_data1' csv data
    """
    data_frame = PartyClassifier(data)
    train_acc, test_acc = data_frame.fit_and_predict_party()
    results(data_frame, train_acc, test_acc)


def tweet_data2_test(data):
    """
    tweet_data2(data) prints results from the machine
    learning model trained on the 'tweet_data2' csv data
    """
    data_frame = PartyClassifier(data)
    train_acc, test_acc = data_frame.fit_and_predict_party()
    results(data_frame, train_acc, test_acc)


def tweet_data3_test(data):
    """
    tweet_data3(data) prints results from the machine learning
    model trained on the 'tweet_data3' csv data
    """
    data_frame = PartyClassifier(data)
    train_acc, test_acc = data_frame.fit_and_predict_party()
    results(data_frame, train_acc, test_acc)


def all_tweet_data(csv_data):
    """
    all_tweet_data(csv_data) prints results from the machine learning
    model trained on csv_data resulting from combining tweet_data1,
    tweet_data2, and tweet_data3. csv_data is a pandas dataframe.
    """
    data = PartyClassifier(csv_data)
    train_acc, test_acc = data.fit_and_predict_party()
    results(data, train_acc, test_acc)


def no_name(csv_data):
    """
    no_name(csv_data) returns the training and testing accuracy
    from a machine learning model trained and tested on the full
    tweet csv, without names
    """
    data = PartyClassifier(csv_data)
    train_acc, test_acc = data.fit_and_predict_party(include_names=False)
    print("Testing Accuracy:", test_acc)
    print("Training Accuracy:", train_acc)


def no_state(csv_data):
    """
    no_state(csv_data) returns the training and testing accuracy
    from a machine learning model trained and tested on the full
    tweet csv, without state
    """
    data = PartyClassifier(csv_data)
    train_acc, test_acc = data.fit_and_predict_party(include_state=False)
    print("Testing Accuracy:", test_acc)
    print("Training Accuracy:", train_acc)


def no_sentiment(csv_data):
    """
    no_sentiment(csv_data) returns the training and testing accuracy
    from a machine learning model trained and tested on the full
    tweet csv, without state
    """
    data = PartyClassifier(csv_data)
    train_acc, test_acc = data.fit_and_predict_party(include_sentiment=False)
    print("Testing Accuracy:", test_acc)
    print("Training Accuracy:", train_acc)


def results(data, train_acc, test_acc):
    """
    results(data, train_acc, test_acc)
    takes in a PartyClassifier object data, as well as training and
    testing accuracies and prints these results in a more legible format.
    """
    print('List of outcomes:')
    print('\t', data._compare_outcomes())
    print()
    print('Accuracy scores:')
    print('\tTraining accuracy:', train_acc)
    print('\tTesting accuracy:', test_acc)
    print()


def main():
    # replace empty string absolute file path to folder
    working_directory = os.listdir('')
    for filename in working_directory:
        #replace empty string with folder name
        file = os.path.join('', filename)
    
    tweet_data1 = pd.read_csv('tweet_data1')
    tweet_data2 = pd.read_csv('tweet_data2')
    tweet_data3 = pd.read_csv('tweet_data3')

    tweet_test_set()
    tweet_data1_test(tweet_data1)
    tweet_data2_test(tweet_data2)
    tweet_data3_test(tweet_data3)

    data_frames = [tweet_data1, tweet_data2, tweet_data3]
    data = pd.concat(data_frames)

    print('All Data:')
    all_tweet_data(data)
    print()

    print('No Names:')
    no_name(data)
    print()

    print('No State:')
    no_state(data)
    print()

    print('No Sentiment:')
    no_sentiment(data)
    print()

if __name__ == '__main__':
    main()
