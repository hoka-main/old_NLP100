def count(file_read):
    box = 0
    for _ in file_read:
        box += 1
    return box


def print_line(zip_type):
    for line, N in zip_type:
        if N < 0:
            break
        else:
            print(line)
            N -= 1


def to_split_row(file, split, indent):
    to_split_list = []
    for line in file:
        list_box = line.split(split)
        to_split_list.append(list_box[indent])
    return to_split_list


def make_line_list(file, split):
    result = []
    for line in file:
        r_strip_line = line.rstrip('\n')
        list_in_list = r_strip_line.split(split)
        num_box3 = list_in_list.pop()
        num_box2 = list_in_list.pop()
        list_in_list.append(int(num_box2))
        list_in_list.append(int(num_box3))
        result.append(list_in_list)
    return result


def parse_mecab(block):
    res = []  # フレーズを形態素解析した結果を入れるリスト
    for line in block.split('\n'):
        if line == '':  # フレーズの終わりを意味する
            return res
        analyzing_source, analyzing_detail = line.split('\t')   # 表層系とそれ以外でリスト化
        analyzing_detail = analyzing_detail.split(',')  # 品詞以下を細かくリスト化
        # マッピング型と指定されているのでdict型に格納
        line_dict = {'surface': analyzing_source,   # 表層形
                     'base': analyzing_detail[6],   # 基本形
                     'pos': analyzing_detail[0],    # 品詞
                     'pos1': analyzing_detail[1]}   # 品詞細分類1
        res.append(line_dict)


def make_phrase_list(mecab_file):  # MeCabファイルを一行ごとにリスト化させる
    with open(mecab_file, 'rt', encoding='utf-8') as phrase:
        phrase_list = phrase.read().split('EOS\n')  # フレーズで区切る
    phrase_list = list(filter(lambda x: x != '', phrase_list))  # 無駄な行を省いてスマートにしちゃう
    return phrase_list


def noun_noun(full_list):
    name = ''
    for line in full_list:
        for index, word in enumerate(line):
            if word['pos'] == '名詞':
                if line[index - 1]['pos'] == '助詞' and line[index - 1]['surface'] == 'の':
                    if line[index - 2]['pos'] == '名詞':
                        name = name + line[index - 2]['surface']\
                               + line[index - 1]['surface']\
                               + line[index]['surface'] + '\n'
    return name
