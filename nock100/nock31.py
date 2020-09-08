import sys
from package import func


'''
def parse_mecab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        (analyzing_source, analyzing_detail) = line.split('\t')
        analyzing_detail = analyzing_detail.split(',')
        if analyzing_detail[0] == '動詞':
            res.append(analyzing_source)
'''


def main():
    args = sys.argv
    args.append('neko.txt.mecab')

    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    for line in phrase_list:
        for dict_line in line:
            if dict_line['pos'] == '動詞':
                print(dict_line['surface'])


if __name__ == '__main__':
    main()
