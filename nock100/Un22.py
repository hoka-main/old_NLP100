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
    pattern = r'^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$'
    result = '\n'.join(re.findall(pattern, read_wiki(args[1], 'イギリス'), re.MULTILINE))
    print(result)


if __name__ == '__main__':
    main()

