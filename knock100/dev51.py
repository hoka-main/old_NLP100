from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import sys
import re
import string


def make_default_title_list():
    file_pass = [
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
        ]

    train = []
    valid = []
    test = []
    read_file = []
    with open(file_pass[0]) as train_id,\
            open(file_pass[1]) as valid_id,\
            open(file_pass[2]) as test_id:
        read_file.append(train_id.read().replace(',', '').replace('.', ''))
        read_file.append(valid_id.read().replace(',', '').replace('.', ''))
        read_file.append(test_id.read().replace(',', '').replace('.', ''))
    for i, items in enumerate(read_file):
        if i == 0:
            for line in items:
                train.append(line)
        elif i == 1:
            for line in items:
                valid.append(line)
        else:
            for line in items:
                test.append(line)
    title_list_of_news_list = [train, valid, test]
    return title_list_of_news_list


def read_dataframe_title():
    file_pass = [
        'ch06/train.txt',
        'ch06/valid.txt',
        'ch06/test.txt'
        ]
    return_file = []
    for file in file_pass:
        text = pd.read_csv(file, sep='\t', names=['TITLE', 'CATEGORY'])
        title = text.TITLE
        return_file.append(title)
    return return_file


def dataframe_of_tfidf(train, valid, test):
    vec_tfidf = TfidfVectorizer()
    dataframe = pd.concat([train, valid, test])  # データを結合している
    vec_tfidf.fit(dataframe)
    return_frame = [vec_tfidf.transform(train), vec_tfidf.transform(valid), vec_tfidf.transform(test)]
    print('Vocabulary size: {}'.format(len(vec_tfidf.vocabulary_)))
    # print('Vocabulary content: {}'.format(vec_tfidf.vocabulary_))
    # print(return_frame)
    dataframe1 = pd.DataFrame(return_frame[0].toarray(), columns=vec_tfidf.get_feature_names())
    dataframe2 = pd.DataFrame(return_frame[1].toarray(), columns=vec_tfidf.get_feature_names())
    dataframe3 = pd.DataFrame(return_frame[2].toarray(), columns=vec_tfidf.get_feature_names())
    dataframe = [dataframe1, dataframe2, dataframe3]
    return dataframe


def main():
    title_frame = read_dataframe_title()
    data = dataframe_of_tfidf(title_frame[0], title_frame[1], title_frame[2])  # データフレーム形式でタイトルを抽出する
    # title_list = make_default_title_list()  # 出現単語を登録し、三つのデータに分割したリストを出力
    save_file_pass_list = [
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
        ]
    dataframe_list = []

    for file_pass, news in zip(save_file_pass_list, data):
        print(news)
        news.to_csv(file_pass, sep='\t', index=False)
    # データフレームにtfidfデータを当て込みファイルに保存する
    '''
    tfidf_vec = TfidfVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
    tfidf_train = tfidf_vec.fit_transform(train)
#    tfidf_valid = tfidf_vec.fit_transform(valid)
#    tfidf_test = tfidf_vec.fit_transform(test)
    print(tfidf_vec.vocabulary_)
    print(tfidf_train)
#    print(tfidf_vec.get_feature_names())
    '''


if __name__ == '__main__':
    main()
