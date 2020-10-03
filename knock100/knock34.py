from package import func
import sys
import knock30


def noon_find(full_list):
    noon_list = []
    counter = 0
    for line in full_list:
        for index, word in enumerate(line):
            if word['pos'] == '名詞':
                counter += 1
            elif counter == 1:
                counter -= 1
            else:
                noon_0 = ''
                while counter > 0:
                    noon_0 = noon_0 + line[index - counter]['surface']
                    if counter == 1:
                        noon_list.append(noon_0)
                    counter -= 1

    return noon_list
    # 名詞を検出後、名詞が連続した回数をカウントし、それをもとに連なった名詞群を抽出し、
    # 連なった名詞群をリストに入れて保存してそれを返す関数。
    # 名詞が連続しない場合はカウントを戻してスルーさせる


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    phrase_list = [knock30.parse_mecab(phrase)
                   for phrase in knock30.make_phrase_list(args[1])]
    for items in noon_find(phrase_list):
        print(items)


if __name__ == '__main__':
    main()
