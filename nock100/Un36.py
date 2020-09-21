import sys
import Un35
import nock30
import numpy
from matplotlib import pyplot
# import japanize_matplotlib  # Pycharm用


def pass_by_value(combo):
    new_phrase = []

    return new_phrase


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


def plot(plot_keys, plot_items, png):
    pyplot.bar(plot_keys, plot_items)
    pyplot.show()
    pyplot.savefig(png)


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    plt_items = []
    plt_keys = []
    counter = 9

    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]

    removed_phrase_list = remove_items(phrase_list, '記号')

    for dict_box, items in Un35.word_pop_frequency(removed_phrase_list):
        plt_keys.append(dict_box)
        plt_items.append(items)
        print(dict_box, items)
        if counter == 0:
            break
        counter -= 1

    plot(plt_keys, plt_items, "graph36.png")


if __name__ == '__main__':
    main()
