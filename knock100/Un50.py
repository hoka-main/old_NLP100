import sys
import csv
import random
import math

'''
def read_csv(csv):
    with open(csv, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        for row in spam_reader:
            print(', '.join(row))
'''


def file_writer(data, file_name):
    with open(file_name, mode='w') as writing_file:
        for line in data:
            for line2 in line:
                writing_file.write(line2)
                writing_file.write('\t')
            writing_file.write('\n')
    # 受け取ったデータをtabで区切りながらデータを入力する関数。
    # データ一行ごとに改行し、受け取ったデータをごちゃまぜにならないようにしている。


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


def main():
    args = sys.argv
    args.append('newsCorpora.csv')
    args.append('2pageSessions.scv')
    target_publisher = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
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
        remaining_count.append(math.floor(percent80))
        remaining_count.append(int((len(target_news_list) - remaining_count[0]) / 2))
        remaining_count.append(int(len(target_news_list) - (remaining_count[0] + remaining_count[1]) - 3))
        print(remaining_count)  # 確認用
        # 抽出したデータを[約80%][残りの20%　/2][残り]でファイルに書き込む回数を決める
    write_data(remaining_count, file_name_list, target_news_list)


if __name__ == '__main__':
    main()
