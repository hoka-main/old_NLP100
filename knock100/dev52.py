from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib


def Lg():
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
    data = []
    for x, y in zip(feature_txt_pass, default_txt_pass):
        x_table = pd.read_table(x, header=None, delimiter='\t')
        x_table = x_table.drop(index=0)
        data.append(x_table)
        y_table = pd.read_table(y, header=None, delimiter='\t')[1]
        data.append(y_table)
    return data


def main():
    Log = Lg()
    x_train = Log[0]
    y_train = Log[1]
    clf = LogisticRegression(random_state=123, max_iter=10000)
    print(clf.fit(x_train, y_train))
    joblib.dump(clf, 'ch06/model.joblib')


if __name__ == '__main__':
    main()
