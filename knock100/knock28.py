import sys
import re
from package import func_wiki

args = sys.argv
args.append('ch03/ch03/jawiki-country.json.gz')


def remove_markup_link(text_date):
    pattern = r'\'{2,5}'
    text_date = re.sub(pattern, '', text_date)

    # 内部リンク
    pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    text_date = re.sub(pattern, r'\1', text_date)

    # テンプレート
    # 他元首等氏名2: {{仮リンク|リンゼイ・ホイル|en|Lindsay Hoyle}}
    pattern = r'\{\{(?:lang|仮リンク)??(?:[^|]*?\|)*?([^|]*?)\}\}'
    text_date = re.sub(pattern, r'\1', text_date)

    # マークアップ削除
    pattern = r'\[\[(?:.*?\|)([^|]*?)\]\]'
    text_date = re.sub(pattern, r'\1', text_date)

    # [.*?]削除
    pattern = r'\[.*?\]'
    text_date = re.sub(pattern, '', text_date)

    # 外部リンク
    pattern = r'https?://[!?\-\.\w=&%\[\]/]+'
    text_date = re.sub(pattern, '', text_date)

    # HTMLタグ
    pattern = r'<.+?>'
    text_date = re.sub(pattern, '', text_date)

    return text_date


def main():
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス'), re.MULTILINE + re.DOTALL)

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))

    result_exe = {field: remove_markup_link(items) for field, items in result.items()}
    for field, items in result_exe.items():
        print(field + ' ' + items)


if __name__ == '__main__':
    main()
