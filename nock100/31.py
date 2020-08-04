import sys
from package import func
args = sys.argv
args.append('neko.txt.mecab')

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


def do(mecab_file):
    with open(mecab_file, 'rt', encoding='utf-8') as phrase:
        phrase_list = phrase.read().split('EOS\n')
    phrase_list = list(filter(lambda x: x != '', phrase_list))
    return phrase_list
'''


def main():
    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    for line in phrase_list:
        for dict_line in line:
            if dict_line['pos'] == '動詞':
                print(dict_line['surface'])


if __name__ == '__main__':
    main()
