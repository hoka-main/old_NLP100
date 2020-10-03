import sys
import re
from package import func_wiki

args = sys.argv
args.append('jawiki-country.json.gz')


def remove_markup_link(text_date):
    pattern = r'\'{2,5}'
    text_date = re.sub(pattern, '', text_date)

    pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    text_date = re.sub(pattern, r'\1', text_date)

    return text_date


def main():
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス'), re.MULTILINE + re.DOTALL)

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))

    result_exe = {field: remove_markup_link(items) for field, items in result.items()}
    for field, items in result_exe.items():
        print(field + ':' + items)


if __name__ == '__main__':
    main()
