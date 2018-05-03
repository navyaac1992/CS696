"""
Exercise 11 - sklearn and pickle


1) Write a definition called "forest_predictor". This definition should:
    - accept one mandatory string argument, a string corresponding to the file path of the CSV file to be read
    - accept one mandatory integer argument, the column containing the classification values (0 based),
            this column should be removed from your training data and stored in its own list
    - accept **kwargs for the cases:
        - header = bool   -> if True: remove the first row after reading the CSV file
        - save = string   -> check if a file with the name exists, if so, load it with pickle and do not train
            a new classifier, if the file does not exist, train a classifier and save it to this location with pickle
        - test = 2d list  -> predict the classifications of this test data set and print the resulting list
    - always return the classifier object
    - check for **kwargs using kwargs.get() and default to False or None!
        EX: header_exists = kwargs.get('header', False)
        NOT: header_exists = kwargs['header']  # crashes if header was not specified
"""

import pickle
import os.path
from sklearn.ensemble import RandomForestClassifier

x = ''
y = ''


def forest_predictor(file_name, classify_column, **kwargs):

    with open(file_name, 'r') as infile:
        data = [line.replace('\n', '').split(',') for line in infile]

    if kwargs.get('header', False):
        data = data[1:]

    csvdata = [line[:classify_column] for line in data]
    classification = [line[classify_column] for line in data]

    stored_file = kwargs.get('save', None)
    if os.path.exists(stored_file):
        with open(stored_file, 'rb') as infile:
            clf = pickle.load(infile)
    else:
        clf = RandomForestClassifier(n_estimators=500)

    clf = clf.fit(csvdata, classification)
    testdata = kwargs.get('test', None)

    print(clf.predict(testdata))

    if stored_file is not None:
        with open(stored_file, 'wb') as outfile:
            pickle.dump(clf, outfile)

    return clf


if __name__ == '__main__':
    # This example uses the training and testing data from lecture_11, a 'large_dataset.csv' is also available, but not required
    clf = forest_predictor('simple_data.csv', 2, header=True, save='saves/random_forest.p',
                           test=[[15, 0], [18, 60000], [80, 30000]])
    # should print ['0', '1', '1'] and return the classifier so that feature_importances_ can be printed
    print(clf.feature_importances_)