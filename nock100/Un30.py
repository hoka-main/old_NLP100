import sys
args = sys.argv
args.append('neko.txt.mecab')


def parse_mecab(block):
    # フレーズを形態素解析した結果を入れるリスト
    res = []

    for line in block.split('\n'):
        if line == '':  # フレーズの終わりを意味する
            return res
        analyzing_source, analyzing_detail = line.split('\t')
        analyzing_detail = analyzing_detail.split(',')
        # マッピング型と指定されているのでdict型に格納
        line_dict = {'surface': analyzing_source,   # 表層形
                     'base': analyzing_detail[6],   # 基本形
                     'pos': analyzing_detail[0],    # 品詞
                     'pos1': analyzing_detail[1]}   # 品詞細分類1
        res.append(line_dict)


def do(mecab_file):
    with open(mecab_file, 'rt', encoding='utf-8') as phrase:
        # フレーズで切り取って扱いやすくする
        phrase_list = phrase.read().split('EOS\n')
    # 無駄な行を省いてスマートにしちゃう
    phrase_list = list(filter(lambda x: x != '', phrase_list))
    return phrase_list


def main():
    text = args[1]
    phrase_list = do(text)
    phrase_list = [parse_mecab(phrase) for phrase in phrase_list]
    for line in phrase_list:
        for line2 in line:
            print(line2)


if __name__ == '__main__':
    main()
