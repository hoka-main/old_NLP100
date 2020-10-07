import sys
import re
from package import func_wiki

args = sys.argv
args.append('ch03/ch03/jawiki-country.json.gz')


def main():
    pattern = r'\[\[ファイル:(.+?)\|'
    result = '\n'.join(re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス')))

    print(result)


if __name__ == '__main__':
    main()

