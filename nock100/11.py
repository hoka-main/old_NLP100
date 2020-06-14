# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ

with open('popular-names.txt') as f:
    for date in f:
        print(date.replace("\t", " "))
