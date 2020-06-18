import sys

args = sys.argv
print(args)
count = 0

with open(args[1]) as file_read:

    for _ in file_read:
        count += 1

print(count)
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
