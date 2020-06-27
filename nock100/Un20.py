import sys
import json
import tarfile
from collections import OrderedDict
import pprint

args = sys.argv


with tarfile.open('jawiki-country.json.gz') as tar:
    for i in tar.getmembers():
        if i.name[0] == '/' or i.name[0:2] == '..':
            print('外のディレクトリに展開されるかも。')
            exit()
    tar.extractall()