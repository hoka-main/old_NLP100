import sys
from package import func
from collections import Counter


def word_pop_frequency(phrase_list):
    phrase = []
    for line in phrase_list:
        for line2 in line:
            phrase.append(line2['surface'])
    phrase_dict = sorted(Counter(phrase).items(), key=lambda x:x[1], reverse=True)
    return phrase_dict


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    for dict_box in word_pop_frequency(phrase_list):
        print(dict_box)


if __name__ == '__main__':
    main()
