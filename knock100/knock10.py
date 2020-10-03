import sys


def count_line(file):
    box = 0
    for _ in file:
        box += 1
    return box


args = sys.argv
txt = 'コマンドラインでテキストファイルを指定してください'
args.append(txt)
if args[1] == txt:
    print(args[1])
else:
    with open(args[1]) as file_read:
        print(count_line(file_read))
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
# コマンド
#  wc /mnt/c/users/81804/PycharmProjects/knock100/knock10.py
