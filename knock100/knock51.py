from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from tqdm import tqdm
import pandas as pd
import sys
import re
import string


def read_dataframe_title():
    file_pass = [
        'ch06/train.txt',
        'ch06/valid.txt',
        'ch06/test.txt'
        ]
    return_file = []
    for file in file_pass:
        text = pd.read_csv(
            file,
            sep='\t',
            header=0,
            names=['TITLE', 'CATEGORY']
        )
        title = text.TITLE
        return_file.append(title)
    return return_file


def dataframe_of_tfidf(title_frame):
    train = title_frame[0]
    valid = title_frame[1]
    test = title_frame[2]
    vec_tfidf = TfidfVectorizer()
    dataframe = pd.concat([train,
                           valid,
                           test]
                          )  # データを結合している
    vec_tfidf.fit(dataframe)
    return_frame = [vec_tfidf.transform(train),
                    vec_tfidf.transform(valid),
                    vec_tfidf.transform(test)
                    ]
    print('Vocabulary size: {}'.format(len(vec_tfidf.vocabulary_)))
    # print('Vocabulary content: {}'.format(vec_tfidf.vocabulary_))
    # print(return_frame)
    dataframe1 = pd.DataFrame(return_frame[0].toarray(), columns=vec_tfidf.get_feature_names())
    dataframe2 = pd.DataFrame(return_frame[1].toarray(), columns=vec_tfidf.get_feature_names())
    dataframe3 = pd.DataFrame(return_frame[2].toarray(), columns=vec_tfidf.get_feature_names())
    dataframe = [dataframe1, dataframe2, dataframe3]
    return dataframe


def dataframe_of_count(title_frame):
    train = title_frame[0]
    valid = title_frame[1]
    test = title_frame[2]
    dataframe = pd.concat([train, valid, test])
    vec_count = CountVectorizer()
    vec_count.fit(dataframe)
    transform_dataframe = [vec_count.transform(train),
                           vec_count.transform(valid),
                           vec_count.transform(test)
                           ]
    print('Vocabulary size: {}'.format(len(vec_count.vocabulary_)))
    print('Vocabulary content: {}'.format(vec_count.vocabulary_))
    data_frame1 = pd.DataFrame(transform_dataframe[0].toarray(), columns=vec_count.get_feature_names())
    data_frame2 = pd.DataFrame(transform_dataframe[1].toarray(), columns=vec_count.get_feature_names())
    data_frame3 = pd.DataFrame(transform_dataframe[2].toarray(), columns=vec_count.get_feature_names())
    data_frame = [data_frame1, data_frame2, data_frame3]
    return data_frame


def to_tsv(data):
    save_file_pass_list = (
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
        )
    for file_pass, news in zip(save_file_pass_list, data):
        news.to_csv(file_pass, sep='\t', index=False)


def main():
    title_frame = read_dataframe_title()
    # データフレーム形式でタイトルを取得

    data = dataframe_of_count(title_frame)
    # 学習・検証・評価データから特徴量を取得しを作成する

    print(data[0], '\n', data[1], '\n', data[2])

    to_tsv(data)
    # データフレームをファイルに保存する


if __name__ == '__main__':
    main()
