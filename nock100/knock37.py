import sys
import knock30
import knock35
from collections import Counter
import knock36


def find_cat(phrase_list, surface):
    new_phrase_list = []
    for line in phrase_list:
        for index, phrase_surface in enumerate(line):
            if phrase_surface['surface'] == surface:
                new_phrase_list.append(line)
    return new_phrase_list


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    counter = 9
    plot_keys = []
    plot_items = []

    phrase_list = [knock30.parse_mecab(phrase)
                   for phrase in knock30.make_phrase_list(args[1])]
    removed_phrase_list = knock36.remove_items(phrase_list, '記号')
    # 36と同じく記号を指定し、記号をカウントしない
    new_phrase_list = find_cat(removed_phrase_list, '猫')
    # 「猫」を含む行を抽出する
    count_list = []
    for line in new_phrase_list:
        for phrase_surface in line:
            if phrase_surface['surface'] == '猫':
                continue
            count_list.append(phrase_surface['surface'])
    # すべての「猫」以外の単語をリストに追加していく
    for phrase, count in knock35.word_pop_frequency(count_list):
        plot_keys.append(phrase)
        plot_items.append(count)
        print(phrase, count)
        if counter == 0:
            break
        counter -= 1
    # 35の表層形のみを抽出する関数を使って表層形のみ抽出・降順にソートし、
    # 上から10個の単語を表示している（表示しなくともよいが確認のため）
    knock36.plot(plot_keys, plot_items, 'graph37.png')
    # 36の関数を使ってグラフに起こす


if __name__ == '__main__':
    main()
