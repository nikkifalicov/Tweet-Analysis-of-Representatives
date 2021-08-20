"""
Nikki Falicov
CSE 163 AB
This class takes in scraped TweetCongress data in CSV format, and generates a
machine learning model to try and predict political party based on the various
labels present in the dataframe

Necessary imports:
- sklearn
- TextBlob --> https://textblob.readthedocs.io/en/dev/install.html
- operator
- pandas
"""
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from textblob import TextBlob
from operator import itemgetter
import pandas as pd


class PartyClassifier:
    """
    Uses machine learning to classify tweets from different political
    representatives during the month of July 2021. Contains functionality
    to compare different train/test splits and their outcomes, as well as
    the accuracy score of the model.
    """

    def __init__(self, data):
        """
        initializes a new PartyClassifier object. Takes in a pandas dataframe,
        data, containing scraped tweet data.
        """
        self._data = data.dropna().copy()
        text = self._data['text']
        self._data.loc[:, 'polarity'] = text.apply(
            lambda x: TextBlob(x).sentiment.polarity)
        self._data.loc[:, 'subjectivity'] = text.apply(
            lambda x: TextBlob(x).sentiment.subjectivity)

    def get_column_names(self):
        """
        get_column_name() returns the column names within the data of the
        current PartyClassifier object
        """
        return self._data.columns

    def _compare_outcomes(self):
        """
        compare_outcomes() compares outcomes for different train/test splits.
        Returns a list of tuples in format (accuracy score, split).
        This list is sorted from greatest to least based on accuracy score
        on test data. Accuracy score is a float ranging from 0 to 100
        indicating the percentage of test data classified correctly
        """
        # make list of the various test sizes from 0.1 to 0.9
        test_sizes = [x/10 for x in range(1, 10)]
        outcomes = []
        for test_data_size in test_sizes:
            train_acc, test_acc = self.fit_and_predict_party(
                test_data_size=test_data_size)
            outcomes.append((test_acc, test_data_size))
        sorted_outcomes = sorted(outcomes, key=itemgetter(0), reverse=True)
        return sorted_outcomes

    def fit_and_predict_party(self, test_data_size=0.2,
                              include_names=True, include_state=True,
                              include_sentiment=True):
        """
        fit_and_predict_party(test_data_size=0.2, include_names=True
        , include_state=True, include_sentiment=True) takes
        in a test data size (b/t 0 and 1 inclusive) and and whether or not
        to include various features, and returns the accuracy score for
        training data and testing data, in format training_accuracy,
        testing_accuracy. The default value for test_data_size is 0.2,
        indicating a 80%/20% split between training and testing data
        (respectively). default values for include_names, include_state,
        and include_sentiment are True. Assumed that only one of include_names
        ,include_state, and include_sentiment is False at any one given time.
        """
        if include_names is False:
            filtered = self._data.loc[:, ['text', 'party', 'state',
                                          'polarity', 'subjectivity']]
        elif include_state is False:
            filtered = self._data.loc[:, ['name', 'text', 'party',
                                          'polarity', 'subjectivity']]
        elif include_sentiment is False:
            filtered = self._data.loc[:, ['name', 'text', 'party', 'state']]
        else:
            filtered = self._data.loc[:, ['name', 'text' 'state', 'party',
                                          'polarity', 'subjectivity']]
        filtered = filtered.dropna()
        features = filtered.loc[:, filtered.columns != 'party']
        features = pd.get_dummies(features)
        labels = filtered['party']

        features_train, features_test, labels_train, labels_test =\
            train_test_split(features, labels, test_size=test_data_size)
        model = DecisionTreeClassifier()
        model.fit(features_train, labels_train)

        pred_train = model.predict(features_train)
        train_acc = accuracy_score(labels_train, pred_train)

        pred_test = model.predict(features_test)
        test_acc = accuracy_score(labels_test, pred_test)
        return train_acc*100, test_acc*100
