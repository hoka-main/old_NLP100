import sys
from package import func


def main():
    args = sys.argv
    args.append('neko.mecab.txt')
    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    phrase_dict{}
    
    print()


if __name__ == '__main__':
    main()
