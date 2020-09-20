import sys
import nock30
import Un35
from collections import Counter
import Un35
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

    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]
    phrase_list = Un36.remove_items(phrase_list, '記号')
    new_phrase_list = find_cat(phrase_list, '猫')
    count_list = []
    for line in new_phrase_list:
        for phrase_surface in line:
            if phrase_surface['surface'] == '猫':
                continue
            count_list.append(phrase_surface['surface'])
    for count_phrase in Un35.word_pop_frequency(count_list):
        print(count_phrase)


if __name__ == '__main__':
    main()
