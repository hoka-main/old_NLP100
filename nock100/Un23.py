import sys
import gzip
import json
import re

args = sys.argv
args.append('jawiki-country.json.gz')


def read_wiki(file_name, title):

    with gzip.open(file_name, 'r', 'utf-8') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == title:
                return data_json['text']


def main():
    result = []
    pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$'
    for section in re.findall(pattern, read_wiki(args[1], 'イギリス'), re.MULTILINE):
        result.append(section[1] + ':' + str(len(section[0]) - 1))
    for line in result:
        print(line)

    # result = '\n'.join(i[1] + ':' + str(len(i[0]) - 1) for i in re.findall(pattern, text_uk, re.MULTILINE))
    # print(result)


if __name__ == '__main__':
    main()

