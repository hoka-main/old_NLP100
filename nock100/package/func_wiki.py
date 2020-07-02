import gzip
import json


def read_wiki(file_name, title):

    with gzip.open(file_name, 'r', 'utf-8') as data_file:
        for line in data_file:
            data_json = json.loads(line)
            if data_json['title'] == title:
                return data_json['text']


def main_wiki():
    file_name = args[1]
    return read_wiki(file_name, 'イギリス')

