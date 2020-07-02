import sys
import json
import gzip
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
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, read_wiki(args[1], 'イギリス'), re.MULTILINE + re.DOTALL)
    print(template)

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
    for field, items in result.items():
        print(field + ': ' + items)


if __name__ == '__main__':
    main()
