import sys
import re
from package import func_wiki

args = sys.argv
args.append('jawiki-country.json.gz')


def main():
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス'), re.MULTILINE + re.DOTALL)
    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))
    for field, items in result.items():
        print(field + ':' + items)


if __name__ == '__main__':
    main()
