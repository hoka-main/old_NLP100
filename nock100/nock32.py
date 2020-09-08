import sys
from package import func


def main():
    args = sys.argv
    args.append('neko.txt.mecab')

    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    for line in phrase_list:
        for dict_line in line:
            if dict_line['pos'] == '動詞':
                print(dict_line['base'])


if __name__ == '__main__':
    main()
