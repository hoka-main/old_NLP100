from sklearn.linear_model import LogisticRegression
import pandas as pd


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
        default_category = pd.read_table(default_txt, delimiter='\t')['CATEGORY']
        data_set = (feature_table, default_category)
        data_list.append(data_set)
    return data_list


def main():
    log = Lg()  # train=[0] valid=[1] test=[2] : feature=[0] default=[1]
    feature_train = log[0][0]
    train_category = log[0][1]
    clf = LogisticRegression(random_state=123, max_iter=10000)
    clf.fit(feature_train, train_category)
    print(clf.fit(feature_train, train_category))


if __name__ == '__main__':
    main()
