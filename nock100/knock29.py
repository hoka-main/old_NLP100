import sys
import re
from package import func_wiki
import json
import urllib.parse, urllib.request


args = sys.argv
args.append('jawiki-country.json.gz')


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


def request_url(result):

    flag = result['国旗画像']
    url = 'https://www.mediawiki.org/w/api.php?' \
          + 'action=query' \
          + '&titles=File:' + urllib.parse.quote(flag) \
          + '&format=json' \
          + '&prop=imageinfo' \
          + '&iiprop=url'

    request = urllib.request.Request(url,
                                     headers={'User-Agent': 'knock100(@hoka)'})
    connection = urllib.request.urlopen(request)
    date = json.loads(connection.read().decode())

    # print(date)
    # {'continue':{'iistart': '2019-09-10T16:52:58Z', 'continue': '||'},
    # 'query':{'pages':
    #           {'-1':
    #               {'ns': 6,
    #                'title': 'File:Flag of the United Kingdom.svg',
    #                'missing': '',
    #                'known': '',
    #                'imagerepository': 'shared',
    #                'imageinfo': [
    #                 {'url': 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg',
    #                  'descriptionurl': 'https://commons.wikimedia.org/wiki/File:Flag_of_the_United_Kingdom.svg',
    #                  'descriptionshorturl': 'https://commons.wikimedia.org/w/index.php?curid=347935'
    #                 }
    #                             ]
    #               }
    #           }
    #         }
    # }
    url = date['query']['pages'].popitem()[1]['imageinfo'][0]['url']
    return url


def main():
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, func_wiki.read_wiki(args[1], 'イギリス'), re.MULTILINE + re.DOTALL)

    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    result = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))

    result_exe = {field: remove_markup_link(items) for field, items in result.items()}

    # ここから
    url = request_url(result_exe)
    print(url)


if __name__ == '__main__':
    main()
