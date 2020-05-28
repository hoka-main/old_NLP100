# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ


def cipher(etc):
    # etc_list = []
    result = ''
    # for index in range(0, len(etc)):
    for Cha in etc:

        if Cha.islower():
            # etc_list.insert(index, chr(219-ord(etc[index])))
            code = 219-ord(Cha)
            code_cha = chr(code)
            result += code_cha

        else:
            # etc_list.insert(index, etc[index])
            result += Cha

    # for index2 in range(0, len(etc)):
        # result += etc_list[index]
    return result


sample = 'Hello World'
test = cipher(sample)
print('暗号文　＝', test)

test = cipher(test)
print('複合文　＝', test)
