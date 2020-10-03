import sys
import CaboCha


def main():
    c = CaboCha.Parser()

    sentence = '太郎はこの本を次郎を見た女性に渡した。'
    print(c.parseToString(sentence))
    tree = c.parse(sentence)
    print(tree.toString(CaboCha.FORMAT_TREE))
    print(tree.toString(CaboCha.FORMAT_LATTICE))


if __name__ == '__main__':
    main()
