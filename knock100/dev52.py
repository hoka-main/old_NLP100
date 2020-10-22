from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib


def Lg():
    feature_txt_pass = 'ch06/train.feature.txt'
    default_txt_pass = 'ch06/train.txt'

    x_train = pd.read_table(feature_txt_pass, header=None, delimiter='\t')
    x_train = x_train.drop(index=0)
    y_train = pd.read_table(default_txt_pass, header=None, delimiter='\t')[1]
    train = [x_train, y_train]
    return train


def main():
    train = Lg()
    x_train = train[0]
    y_train = train[1]
    clf = LogisticRegression(random_state=123, max_iter=10000)
    print(clf.fit(x_train, y_train))
    joblib.dump(clf, 'ch06/model.joblib')


if __name__ == '__main__':
    main()
