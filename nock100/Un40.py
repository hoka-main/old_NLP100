import sys
import CaboCha


def main():
    c = CaboCha.Parser()
    args = sys.argv
    args.append('ai.ja.txt')
    sentence = 'ai.ja.txt'

    print(c.parseToString(sentence))
    tree = c.parse(sentence)
    print(tree.toString(CaboCha.FORMAT_TREE))
    print(tree.toString(CaboCha.FORMAT_LATTICE))


if __name__ == '__main__':
    main()
