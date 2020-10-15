from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import sys
import re
import string


def make_default_title_list(title_file_list):
    train = []
    valid = []
    test = []

    for i, items in enumerate(title_file_list):
        items.replace(',', '').replace('.', '')
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


def test_def(args):
    return_file = []
    del args[0]
    for file in args:
        text = pd.read_csv(file, sep='\t', names=['TITLE', 'CATEGORY'])
        title = text.TITLE
        return_file.append(title)
    return return_file


def dataframe_of_tfidf(sample):
    vec_tfidf = TfidfVectorizer()
    x = vec_tfidf.fit_transform(sample)
    print('Vocabulary size: {}'.format(len(vec_tfidf.vocabulary_)))
    # print('Vocabulary content: {}'.format(vec_tfidf.vocabulary_))

    dataframe = pd.DataFrame(x.toarray(), columns=vec_tfidf.get_feature_names())
    return dataframe


def main():
    args = sys.argv
    args.append('ch06/train.txt')
    args.append('ch06/valid.txt')
    args.append('ch06/test.txt')

    save_file_pass_list = [
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
    ]
    data = test_def(args) # タイトルを抽出する

    title_list = make_default_title_list(data) # データを分ける

    for file_pass, news in zip(save_file_pass_list, title_list):
        dataframe = dataframe_of_tfidf(news)
        dataframe.to_csv(file_pass)
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
