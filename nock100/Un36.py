import sys
import re
from collections import Counter
import Un35
import nock30
import numpy
from matplotlib import pyplot


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]
    counter = 9

    # kigou = ["。", "、", "「", "」"]
    # regex = ""
    # re.sub(regex, surface)
    # pattern = re.compile('[「」。、]+')
    for index, dict_box in enumerate(Un35.word_pop_frequency(phrase_list)):
        print(dict_box)
        if index == counter:
            break
    pyplot.plot(dict_box)
    pyplot.show()


if __name__ == '__main__':
    main()
