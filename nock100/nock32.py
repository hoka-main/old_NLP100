import sys
import nock30


def main():
    args = sys.argv
    args.append('neko.txt.mecab')

    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]
    # 形態素解析のリストを作成
    for line in phrase_list:
        for dict_line in line:
            if dict_line['pos'] == '動詞':
                print(dict_line['base'])
    # リストに含まれる動詞の原形を表示


if __name__ == '__main__':
    main()
