import sys
import re
from package import func_wiki

args = sys.argv
args.append('jawiki-country.json.gz')


def main():
    pattern = r'\[\[Category:(.*?)(?:\|.*)?\]\]'
    result = '\n'.join(re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス'), re.MULTILINE))
    print(result)


if __name__ == '__main__':
    main()

