count = 0
with open('popular-names.txt') as fileread:
    for _ in fileread:
        count += 1
print(count)
# 行数をカウントせよ．確認にはwcコマンドを用いよ．