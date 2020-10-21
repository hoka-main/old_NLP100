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

    x_train = pd.read_table(feature_txt_pass[0], header=None, delimiter='\t')
    x_train = x_train.drop(index=0)
    y_train = pd.read_table(default_txt_pass[0], header=None, delimiter='\t')[1]
    clf = LogisticRegression(random_state=123, max_iter=10000)
    print(clf.fit(x_train, y_train))


if __name__ == '__main__':
    main()
