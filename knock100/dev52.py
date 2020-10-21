from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib


def main():
    feature_txt_pass = [
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
    ]
    default_txt_pass = [
        'ch06/train.txt',
        'ch06/valid.txt',
        'ch06/test.txt'
    ]

    x_train = pd.read_table(feature_txt_pass[0], header=None)
    y_train = pd.read_table(default_txt_pass[0], header=None)[1]
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    joblib.dump(clf, 'ch06/model.joblib')


if __name__ == '__main__':
    main()
