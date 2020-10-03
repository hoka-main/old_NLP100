import sys
import re
from package import func_wiki

args = sys.argv
args.append('jawiki-country.json.gz')

'''
with gzip.open(args[1], 'r', 'utf-8') as data_file:
    for line in data_file:
        data_json = json.loads(line)
        if data_json['title'] == 'イギリス':
            text_UK = data_json['text']
            break


patten = r'^(.*\[\[Category:.*\]\].*)$'
file_name = args[1]
result = '\n'.join(re.findall(patten, text_UK, re.MULTILINE))
print(result)
'''


def main():
    pattern = r'\[\[Category:.*\]\]'
    result = '\n'.join(re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス'), re.MULTILINE))
    print(result)


if __name__ == '__main__':
    main()

