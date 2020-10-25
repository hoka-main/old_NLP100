from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib


def Lg():
    feature_txt_pass = (
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
    )
    default_txt_pass = (
        'ch06/train.txt',
        'ch06/valid.txt',
        'ch06/test.txt'
    )
    data_list = []
    for feature_txt, default_txt in zip(feature_txt_pass, default_txt_pass):
        feature_table = pd.read_table(feature_txt, delimiter='\t')
        default_table = pd.read_table(default_txt, delimiter='\t')['CATEGORY']
        data_set = (feature_table, default_table)
        data_list.append(data_set)
    return tuple_list


def main():
    Log = Lg()  # train=[0] valid=[1] test=[2] x=[0] y=[1]
    x_train = Log[0][0]
    y_train = Log[0][1]
    clf = LogisticRegression(random_state=123, max_iter=10000)
    print(clf.fit(x_train, y_train))
    joblib.dump(clf, 'ch06/model.joblib')


if __name__ == '__main__':
    main()
