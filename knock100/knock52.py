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
    clf = LogisticRegression(random_state=123, max_iter=10000)
    clf.fit(data_list[0][0], data_list[0][1])  # 学習データを使って学習させる
    data_list.insert(0, clf)    # 先頭にfitさせたLogisticファイルを挿入させる
    return data_list


def main():
    log = Lg()  # clf.fit=[0] train=[1] valid=[2] test=[3] : feature=[x][0] default=[x][1]
    print(log[0])


if __name__ == '__main__':
    main()
