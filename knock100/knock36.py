import sys
import knock35
import knock30
import numpy
from matplotlib import pyplot
# import japanize_matplotlib


def pass_by_value(combo):
    new_phrase = []

    return new_phrase
    # 未使用


def remove_items(phrase_list, pos):
    new_phrase = []
    new_phrase_list = []
    for list1 in phrase_list:
        for phrase in list1:
            if phrase['pos'] == pos:
                continue
            new_phrase.append(phrase)
            # pass_by_value(phrase)
        new_phrase_list.append(list(new_phrase))
        new_phrase.clear()
    return new_phrase_list
    # 特定のposを排除する関数。
    # phrase_listに含まれている形態素解析データの指定したpos種類を任意で排除する。
    # 手法としてすべての単語をfor文で回し、指定したposが回って来た時にのみcontinueで飛ばしている。
    # また、list()を使って参照渡しを回避している。


def plot(plot_keys, plot_items, png):
    pyplot.bar(plot_keys, plot_items)
    pyplot.show()
    pyplot.savefig(png)
    # プロットコンフィグ関数。ここで各種調整する。


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    plt_items = []
    plt_keys = []
    counter = 9

    phrase_list = [knock30.parse_mecab(phrase)
                   for phrase in knock30.make_phrase_list(args[1])]

    removed_phrase_list = remove_items(phrase_list, '記号')
    # ここで記号を排除する

    for dict_box, items in knock35.word_pop_frequency(removed_phrase_list):
        plt_keys.append(dict_box)
        plt_items.append(items)
        print(dict_box, items)
        if counter == 0:
            break
        counter -= 1
    # 35のプログラムを実行し、matplotlibに各アイテムを代入している。
    plot(plt_keys, plt_items, "graph36.png")
    # plot関数にデータを入力してファイル名を指定し作成する


if __name__ == '__main__':
    main()
