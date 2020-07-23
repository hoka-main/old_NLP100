import sys
args = sys.argv
args.append('neko.txt.mecab')


def parse_mecab(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        (analyzing_source, analyzing_detail) = line.split('\t')
        analyzing_detail = analyzing_detail.split(',')
        if analyzing_detail[0] == '動詞':
            res.append(analyzing_detail[6])


def do(mecab_file):
    with open(mecab_file, 'rt', encoding='utf-8') as phrase:
        phrase_list = phrase.read().split('EOS\n')
    phrase_list = list(filter(lambda x: x != '', phrase_list))
    return phrase_list


def main():
    text = args[1]
    phrase_list = do(text)
    phrase_list = [parse_mecab(phrase) for phrase in phrase_list]
    print(phrase_list)


if __name__ == '__main__':
    main()
