import sys
from package import func

args = sys.argv
print(args)
with open(args[1]) as file_read:
    Line_count = func.count(file_read)

print(Line_count)
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
