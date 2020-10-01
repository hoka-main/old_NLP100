import sys
import nock30
import nock35
import matplotlib.pyplot as plt


def main():
    args = sys.argv
    args.append('neko.txt.mecab')

    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]
    for line in phrase_list:
        for morphological_analysis in line:
            # print(morphological_analysis)
            pass
    counter = []
    for number in nock35.word_pop_frequency(phrase_list):
        counter.append(number[1])
    print(counter)
    rank = []
    num = []
    for index, number in enumerate(counter):
        rank.append(index + 1)
        num.append(number)
    print(rank, num)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    plt.savefig('graph39')


if __name__ == '__main__':
    main()
