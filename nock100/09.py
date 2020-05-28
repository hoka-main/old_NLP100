# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文
# （例えば”I couldn’t believe that I could actually understand
# what I was reading : the phenomenal power of the human mind .”）
# を与え，その実行結果を確認せよ．


import random

test_text = "I couldn’t believe that I could actually understand what " \
            " I was reading : the phenomenal power of the human mind ."

print(test_text)

# test_text = test_text.replace('.', '')
# test_text = test_text.replace(',', '')

to_split = test_text.split()
# box = ''
# list_box = []
result_listbox = []
# count = 0
print(to_split)
for box in to_split:
    if len(box) > 4:
        # box0 = box[0]
        # box_1 = box[-1]
        box_center = box[1:-1]
        random_box = random.sample(box_center, len(box_center))
        # box1_1 = ''.join(random_box)
        # test_list = box0, box1_1, box_1
        # joined_Cha = ''.join(test_list)
        joined_Cha = box[0] + ''.join(random_box) + box[-1]
        result_listbox.append(joined_Cha)
    else:
        result_listbox.append(box)


print(result_listbox)
result = ' '.join(result_listbox)
print(result)
