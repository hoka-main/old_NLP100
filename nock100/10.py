import sys


def count(file_read):
    box = 0
    for _ in file_read:
        box += 1
    return box


args = sys.argv
print(args)
with open(args[1]) as file_read:
    Line_count = count(file_read)

print(Line_count)
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
