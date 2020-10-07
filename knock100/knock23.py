import sys
import re
from package import func_wiki

args = sys.argv
args.append('ch03/ch03/jawiki-country.json.gz')


def main():
    result = []
    pattern = r'^(\={2,})\s*(.+?)\s*(\={2,}).*$'
    for section in re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス'), re.MULTILINE):
        result.append(section[1] + ':' + str(len(section[0]) - 1))
    for line in result:
        print(line)

    # result = '\n'.join(i[1] + ':' + str(len(i[0]) - 1) for i in re.findall(pattern, text_uk, re.MULTILINE))
    # print(result)


if __name__ == '__main__':
    main()

