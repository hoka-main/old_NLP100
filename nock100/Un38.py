import sys
import Un35
import nock30
from collections import defaultdict
import matplotlib.pyplot as plt


def extract_words(block):
    return [b['base'] + '_' + b['pos'] + '_' + b['pos1'] for b in block]


def main():
    args = sys.argv
    args.append('neko.txt.mecab')
    phrase_list = [nock30.parse_mecab(phrase)
                   for phrase in nock30.make_phrase_list(args[1])]
    words = [extract_words(brock) for brock in phrase_list]
    print(words)
    d = defaultdict(int)
    for word in words:
        for tag in word:
            d[tag] += 1
    ans = d.values()
    plt.figure(figsize=(8, 8))
    plt.hist(ans, bins=100)
    plt.savefig('ans38.png')


if __name__ == '__main__':
    main()
