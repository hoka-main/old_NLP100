# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ
import sys

args = sys.argv
print(args)

with open(args[1]) as f:

    for date in f:
        print(date.replace("\t", " "))
