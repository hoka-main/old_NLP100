import sys
import nock30
import Un35
from collections import Counter
import Un36


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

    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]
    removed_phrase_list = Un36.remove_items(phrase_list, '記号')
    new_phrase_list = find_cat(removed_phrase_list, '猫')
    count_list = []
    for line in new_phrase_list:
        for phrase_surface in line:
            if phrase_surface['surface'] == '猫':
                continue
            count_list.append(phrase_surface['surface'])
    for phrase, count in Un35.word_pop_frequency(count_list):
        plot_keys.append(phrase)
        plot_items.append(count)
        print(phrase, count)
        if counter == 0:
            break
        counter -= 1

    Un36.plot(plot_keys, plot_items, 'graph37.png')


if __name__ == '__main__':
    main()
