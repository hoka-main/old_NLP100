import sys
from package import func
from collections import Counter


def phrase_key_list(phrase_list, key):
    phrase = []
    for line in phrase_list:
        for items in line:
            phrase.append(items[key])
    return phrase
    # phrase_listに含まれる形態素解析の任意のキーのみをリストにして返す関数。


def word_pop_frequency(phrase):
    if isinstance(phrase[0], list):
        phrase = phrase_key_list(phrase, 'surface')
    phrase_list = sorted(Counter(phrase).items(), key=lambda x:x[1], reverse=True)
    return phrase_list
    # phrase_key_listで表層形(surface)を指定し、phraseをすべて表層形にしたのちに、
    # 同じものをカウントし、降順でソートしたリストを返す関数。


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    for dict_box, dict_item in word_pop_frequency(phrase_list):
        print(dict_box, dict_item)
    # print(word_pop_frequency(phrase_list))
    # word_pop_frequencyを実行して得たリストから単語、出現回数をprintする。


if __name__ == '__main__':
    main()
