import sys
import nock30


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

    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]
    # nock30で使用した形態素のリスト表現
    for line in phrase_list:
        for dict_line in line:
            if dict_line['pos'] == '動詞':
                print(dict_line['surface'])
    # phrase‗listに含まれる動詞のsurfaceを表示


if __name__ == '__main__':
    main()
