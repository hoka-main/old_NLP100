# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ
import sys

args = sys.argv
txt = 'コマンドラインでテキストファイルを指定してください'
args.append(txt)
if args[1] == txt:
    print(txt)
else:
    with open(args[1]) as f:
        for date in f:
            print(date.replace("\t", " "))

# コマンド
# expand /mnt/c/users/81804/PycharmProjects/nock100/popular-names.txt
