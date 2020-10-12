import urllib.request
from urllib.request import urlopen, Request
from urllib.error import URLError
import time
import sys


def main():
    args = sys.argv
    yes_or_no = input('ダウンロードを開始しますか？(y/n):')
    if yes_or_no == 'y':
        print(args[1], 'のダウンロードを開始します。')
        with open(args[1], mode='r') as file:
            urls = file.read().split()
            for index, url in enumerate(urls):
                title = 'pdfs/' + str(index) + '.pdf'
                print(url, 'を', title, 'として保存しています...')

                try:
                    urllib.request.urlretrieve(url, title)
                    time_s = len(urls) - index
                    print('ファイルを保存しました。     残りファイル数:', time_s, '   残り時間:', time_s * 5 // 60, '/min')

                    time.sleep(5)
                except URLError as e:
                    if hasattr(e, 'reason'):
                        print('We failed to reach a server.')
                        print('Reason: ', e.reason)
                    elif hasattr(e, 'code'):
                        print("The server couldn't fu.fill the request.")
                        print('Error code: ', e.code)

    elif yes_or_no == 'n':
        print('ダウンロードを中断しプログラムを終了します')
    else:
        print('y or n を入力してください')


if __name__ == '__main__':
    main()
