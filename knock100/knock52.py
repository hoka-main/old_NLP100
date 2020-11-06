from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle


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
        feature_table = pd.read_table(
            feature_txt, delimiter='\t')
        default_category = pd.read_table(
            default_txt, delimiter='\t')['CATEGORY']
        data_set = (feature_table, default_category)
        data_list.append(data_set)
    data_dict = {'train_feature': data_list[0][0],
                 'train_category': data_list[0][1],
                 'valid_feature': data_list[1][0],
                 'valid_category': data_list[1][1],
                 'test_feature': data_list[2][0],
                 'test_category': data_list[2][1]
                 }
    return data_dict


def fit():
    log = Lg()
    clf = LogisticRegression(random_state=123, max_iter=10000)
    clf.fit(log['train_feature'], log['train_category'])
    # 学習データを使って学習させる
    log['clf'] = clf
    # fitさせたLogisticファイルを挿入する
    return log


def save_clf(clf):
    file_path = 'ch06/finalized_model.sav'
    pickle.dump(clf, open(file_path, 'wb'))


def load_clf():
    file_path = 'ch06/finalized_model.sav'
    return pickle.load(open(file_path, 'rb'))


def main():
    log = fit()
    print(log['clf'])
    save_clf(log['clf'])


if __name__ == '__main__':
    main()
