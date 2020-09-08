import sys
from collections import Counter
import Un35
import nock30


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]

    for index, dict_box in enumerate(Un35.word_pop_frequency(phrase_list)):
        print(dict_box)
        if index == 10:
            break


if __name__ == '__main__':
    main()
