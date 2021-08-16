"""
Nikki Falicov
CSE 163 AB
This class contains code to test and view results from the machine
learning model in PartyClassifier.py

necessary imports:
    - pandas
    - PartyClassifier
"""
from PartyClassifier import PartyClassifier
import pandas as pd


def tweet_test_set():
    """
    tweet_test_set() prints results from the machine learning
    model trained on the 'tweet_test' csv file
    """
    test_csv = pd.read_csv('tweet_test')
    test = PartyClassifier(test_csv)
    print(test.get_column_names())
    train_acc, test_acc = test.fit_and_predict_party()
    train_acc_names, test_acc_names = test.fit_and_predict_party()
    results(test, train_acc, test_acc, train_acc_names, test_acc_names)


def tweet_data1():
    """
    tweet_data1() prints results from the machine learning
    model trained on the 'tweet_data1' csv file
    """
    data = PartyClassifier(pd.read_csv('tweet_data1'))
    train_acc, test_acc = data.fit_and_predict_party()
    train_acc_names, test_acc_names = data.fit_and_predict_party()
    results(data, train_acc, test_acc, train_acc_names, test_acc_names)


def tweet_data2():
    """
    tweet_data2() prints results from the machine learning
    model trained on the 'tweet_data2' csv file
    """
    data = PartyClassifier(pd.read_csv('tweet_data2'))
    train_acc, test_acc = data.fit_and_predict_party()
    train_acc_names, test_acc_names = data.fit_and_predict_party()
    results(data, train_acc, test_acc, train_acc_names, test_acc_names)


def tweet_data3():
    """
    tweet_data3() prints results from the machine learning
    model trained on the 'tweet_data3' csv file
    """
    data = PartyClassifier(pd.read_csv('tweet_data3'))
    train_acc, test_acc = data.fit_and_predict_party()
    train_acc_names, test_acc_names = data.fit_and_predict_party()
    results(data, train_acc, test_acc, train_acc_names, test_acc_names)


def all_tweet_data():
    """
    all_tweet_data() prints results from the machine learning
    model trained on csv resulting from combining tweet_data1,
    tweet_data2, and tweet_data3.
    """
    tweet_data1 = pd.read_csv('tweet_data1')
    tweet_data2 = pd.read_csv('tweet_data2')
    tweet_data3 = pd.read_csv('tweet_data3')
    data_frames = [tweet_data1, tweet_data2, tweet_data3]
    data = PartyClassifier(pd.concat(data_frames))
    train_acc, test_acc = data.fit_and_predict_party()
    train_acc_names, test_acc_names = data.fit_and_predict_party()
    results(data, train_acc, test_acc, train_acc_names, test_acc_names)


def results(data, train_acc, test_acc, train_acc_names, test_acc_names):
    """
    results(data, train_acc, test_acc, train_acc_names, test_acc_names)
    takes in a PartyClassifier object data, as well as training and
    testing accuracies for models trained using names as a feature, as
    well as models trained without names as a feature, and prints these
    results in a more legible format.
    """
    print('List of outcomes:')
    print('\t', data._compare_outcomes())
    print()
    print('Accuracy scores without names as a feature:')
    print('\tTraining accuracy:', train_acc)
    print('\tTesting accuracy:', test_acc)
    print()
    print('Accuracy scores with names as a feature:')
    print('\tTraining accuracy:', train_acc_names)
    print('\tTesting accuracy:', test_acc_names)


def main():
    tweet_test_set()
    tweet_data1()
    tweet_data2()
    tweet_data3()
    all_tweet_data()
