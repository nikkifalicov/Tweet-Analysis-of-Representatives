"""
Nikki Falicov
CSE 163 AB
This class takes in scraped TweetCongress data, and generates a machine learning
model to try and predict political party based on the various labels present in
the scraped data
"""
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.base import clone
from scraper import Scraper
from operator import itemgetter
import pandas as pd

"""
contents (approximate):
- make a machine learning model (decision tree classifier)
- compare outcomes of machine learning models

COMMENTS ARE PRELIM
"""
class PartyClassifier:
    
    def __init__(self, data):
        """
        takes in a pandas dataframe
        """
        self._data = data
        #possibly clean text here if needed
    
    def get_column_names(self):
        """
        returns column names within dataframe
        """
        return self._data.columns
    
    def compare_outcomes(self, features, labels):
        """
        takes in the list of features and labels, and returns a list of tuples
        detailing the mean squared error for different splits ranging
        from 0.1 to 0.9 inclusive. returned list is sorted from least
        to greatest by mean squared error.
        """
        # make list of the various test sizes from 0.1 to 0.9
        test_sizes = [x/10 for x in range(1, 10)]
        outcomes = []
        for test_data_size in test_sizes:
            # general algorithm: create a decision tree, and split the data
            # according the current iteration through test size. train and
            # test the model, and store the outcome and the split for that
            # specific model
            model_test = DecisionTreeClassifier()
            features_train, features_test, labels_train, labels_test =\
                train_test_split(features, labels, test_size=test_data_size)
            model_test.fit(features_train, labels_train)
            test_predictions = model_test.predict(features_test)
            error = mean_squared_error(labels_test, test_predictions)
            outcomes.append((error, test_data_size))
        #sort the outcomes by the smallest error
        sorted_outcomes = sorted(outcomes, key=itemgetter(0))
        return sorted_outcomes

    def fit_and_predict_party(self, test_data_size = 0.2):
        """
        creates a machine learning model, with the training/test split
        detailed in parameter, returning the mean squared error
        """
        filtered = self._data.loc[:, ['state', 'text', 'party']]
        filtered = filtered.dropna()
        features = filtered.loc[:, filtered.columns != 'party']
        features = pd.get_dummies(features)
        labels = filtered['party']

        features_train, features_test, labels_train, labels_test =\
            train_test_split(features, labels, test_size=test_data_size)
        model = DecisionTreeClassifier()
        model.fit(features_train, labels_train)
        test_predictions = model.predict(features_test)
        error = mean_squared_error(labels_test, test_predictions)
        return error
    
    def main():
        #pass in the tweet test sets
        print('Objects need to be created for testing/analyses')

    if __name__ == '__main__':
        main()

    
