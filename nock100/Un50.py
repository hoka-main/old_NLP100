import sys
import csv


def read_csv(csv):
    with open(csv, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
        for row in spam_reader:
            print(', '.join(row))


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


def main():
    args = sys.argv
    args.append('newsCorpora.csv')
    args.append('2pageSessions.scv')
    list_box = []
    with open(args[1]) as csv_file:
        reader = csv.reader(csv_file)
        log = []
        for index, line in enumerate(reader):
            print('*********************************************')
            print(line)
            print('***')

            for row in line:
                list_box.extend(row.strip().split('\t'))

            print(list_box[4])
            list_box.clear()
            if index == 17:
                break
#             elif index == 18:
#                 break


        # read_file = csv_file.read()
        # read_file.splitlines()
        # print(read_file[0:10])
        # to_split = read_file.split('\t')
        # print(to_split[0:10])
    # read_csv(args[1])


if __name__ == '__main__':
    main()
