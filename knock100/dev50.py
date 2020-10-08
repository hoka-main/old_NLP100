import sys
import csv
import random
import math
import pandas as pd
from sklearn.model_selection import train_test_split


'''
def read_csv(csv):
    with open(csv, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, 
                                delimiter=' ', quotechar='|')
        for row in spam_reader:
            print(', '.join(row))
'''


def file_writer(data, file_name):
    with open(file_name, mode='w')\
            as writing_file:
        for line in data:
            for line2 in line:
                writing_file.write(line2)
                writing_file.write('\t')
            writing_file.write('\n')
    # 受け取ったデータをtabで区切りながらデータを入力する関数。
    # データ一行ごとに改行し、受け取ったデータを
    # ごちゃまぜにならないようにしている。


def write_data(remaining_count, file_name_list, target_news_list):
    file_list = []
    for count, file_name in zip(remaining_count, file_name_list):
        while count >= 0:
            append_data = target_news_list.pop()
            # print(append_data)
            file_list.append(append_data)
            count -= 1
            # print(count)
        file_writer(file_list, file_name)
        file_list.clear()
    # ファイルに書き込むデータを仕分けてfile_writerにデータを送る関数
    # 書き込むファイル数は3つなので、for文でまとめて書き込むために用意した
    # カウントがそれぞれ約80%、約10％、約10%を指定しており、
    # ファイルネームもあらかじめmain()で用意している
    # ファイルに書き込み終えるたびに使った変数はリセットしている


"""
def split_details_list(csv1):
    with open(csv1, mode='rt') as csv_file:
        news_list = csv_file.read().splitlines()
        news_list_details = []
        for line in news_list:
            news_list_details.append(line.split('\t'))
    return news_list_details


def sub1():
    args = sys.argv
    args.append('newsCorpora.csv')
    args.append('2pageSessions.scv')
    print(args)
    news_list_details = split_details_list(args[1])
    print(news_list_details[17])
    
    # もともとmainで作成していたコード。
    # 手動でcsvファイルを読み込もうとしていたので
    # コード量が多いしまだ途中なので動かない。
"""


def sub2():
    args = sys.argv
    args.append('newsCorpora.csv')
    args.append('2pageSessions.scv')
    target_publisher = ['Reuters', 'Huffington Post',
                        'Businessweek', 'Contactmusic.com',
                        'Daily Mail']
    file_name_list = ['train.txt', 'valid.txt', 'test.txt']

    target_news_list = []
    remaining_count = []
    
    csv.field_size_limit(1000000000)
    # フィールドリミット以上のデータを扱うのでリミッターを緩くする
    with open(args[1], newline='') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            news = []
            line = ', '.join(line)
            line = line.split('\t')
            for row in line:
                news.extend(row.strip().split('\t'))
            # ここまでデータの整形

            for target in target_publisher:
                if target in news[3]:
                    target_news_list.append(list(news))
            # 抜き取りたいデータを全体から抽出する

            '''if index == 100:
                break'''
            # test
        random.shuffle(target_news_list)
        # 抽出したデータをランダムに並び替える
        print(len(target_news_list))    # 確認用
        percent80 = len(target_news_list) * 0.8
        remaining_count.append(
            math.floor(percent80))
        remaining_count.append(
            int((len(target_news_list) - remaining_count[0]) / 2))
        remaining_count.append(
            int(len(target_news_list) -
                (remaining_count[0] + remaining_count[1]) - 3))
        print(remaining_count)  # 確認用
        # 抽出したデータを[約80%][残りの20%　/2][残り]で
        # ファイルに書き込む回数を決める
    write_data(remaining_count, file_name_list, target_news_list)


def test():
    # データの読込
    df = pd.read_csv('ch06/newsCorpora_re.csv', header=None, sep='\t',
                     names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

    # データの抽出
    df = df.loc[
        df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), [
            'TITLE', 'CATEGORY']]

    # データの分割
    train, valid_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=123, stratify=df['CATEGORY'])
    valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True, random_state=123,
                                   stratify=valid_test['CATEGORY'])

    # データの保存
    train.to_csv('ch06/train.txt', sep='\t', index=False)
    valid.to_csv('ch06/valid.txt', sep='\t', index=False)
    test.to_csv('ch06/test.txt', sep='\t', index=False)

    # 事例数の確認
    print('【学習データ】')
    print(train['CATEGORY'].value_counts())
    print('【検証データ】')
    print(valid['CATEGORY'].value_counts())
    print('【評価データ】')
    print(test['CATEGORY'].value_counts())


def main():
    args = sys.argv
    args.append('ch06/newsCorpora_re.csv')
    read_data = pd.read_csv(
        args[1], sep='\t', names=[
            'ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY',
            'STORY', 'HOSTNAME', 'TIMESTAMP'])

    read_data = read_data.loc[
        read_data['PUBLISHER'].isin(
            ['Reuters', 'Huffington Post',
             'Business_week', 'Contact_music.com', 'Daily_Mail']
        ), ['TITLE', 'CATEGORY']
    ]

    train, valid_test = train_test_split(
        read_data, test_size=0.2, shuffle=True, random_state=123,
        stratify=read_data['CATEGORY']
    )

    valid, test = train_test_split(
        valid_test, test_size=0.5, shuffle=True, random_state=123,
        stratify=valid_test['CATEGORY']
    )

    train.to_csv('ch06/train.txt', sep='\t', index=False)
    valid.to_csv('ch06/valid.txt', sep='\t', index=False)
    test.to_csv('ch06/test.txt', sep='\t', index=False)

    print(train['CATEGORY'].value_counts())
    print(valid['CATEGORY'].value_counts())
    print(test['CATEGORY'].value_counts())


if __name__ == '__main__':
    # test()
    main()
