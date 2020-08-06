import sys
from package import func
args = sys.argv
args.append('neko.txt.mecab')
name = []


def search(full_list):
    for i, line in enumerate(full_list):
        for j, word in enumerate(line):
            if word['pos1'] == '連体化':
                name.append(line[i](word['surface']))
    return name


def main():
    phrase_list = [func.parse_mecab(phrase)
                   for phrase in func.make_phrase_list(args[1])]
    print(search(phrase_list))


if __name__ == '__main__':
    main()