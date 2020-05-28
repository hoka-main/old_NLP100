# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ


def cipher(etc):
    etc_list = []
    result = ''
    for index in range(0, len(etc)):
        if etc[index].islower():
            etc_list.insert(index, chr(219-ord(etc[index])))
        else:
            etc_list.insert(index, etc[index])
    for index2 in range(0, len(etc)):
        result += etc_list[index2]
    return result

sample = 'Hello World'
test = cipher(sample)
print(test)

test = cipher(test)
print(test)