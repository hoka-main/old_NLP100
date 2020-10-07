import sys
from package import func


def search(full_list):
    name = ''
    for line in full_list:
        for index, word in enumerate(line):
            if line[index]['pos1'] == '連体化':
                name = name + line[index - 1]['surface'] + \
                       line[index]['surface']
            if line[index - 1]['pos1'] == '連体化':
                name = name + line[index]['surface'] + '\n'
    return name[0:-1]
    # 連体化の「の」を検出してその前後を抽出する手法、今回は未使用


def is_pos(word):
    return word['pos'] == '名詞'


def is_no(word):
    return word['pos'] == '助詞' and word['surface'] == 'の'


def noun_noun(full_list):
    name = ''
    for line in full_list:
        for index, word in enumerate(line):
            # if word['pos'] == '名詞':
            # if line[index - 1]['pos'] == '助詞' and line[index - 1]['surface'] == 'の':
            # if line[index - 2]['pos'] == '名詞':
            if is_pos(word) and is_no(line[index - 1]) and is_pos(line[index - 2]):
                name = name + line[index - 2]['surface'] \
                               + line[index - 1]['surface'] \
                               + line[index]['surface'] + '\n'
    return name
    # 名詞を検出し、その-1が助詞の「の」、その-2が名詞だった場合、
    # その1グループのsurfaceを出力する関数


def main():
    args = sys.argv
    args.append('ch04/neko.txt.mecab')

    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    print(noun_noun(phrase_list))


if __name__ == '__main__':
    main()
