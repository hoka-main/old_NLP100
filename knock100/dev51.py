from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import sys


def test_def(args):
    return_file = []
    del args[0]
    for file in args:
        text = pd.read_csv(file, sep='\t', names=['TITLE', 'CATEGORY'])
        title = text.TITLE
        return_file.append(title)
    return return_file


def main():
    args = sys.argv
    args.append('ch06/train.txt')
    args.append('ch06/valid.txt')
    args.append('ch06/test.txt')
    with open(args[1], mode='r') as train, \
            open(args[2], mode='r') as valid, \
            open(args[3], mode='r') as test:
        pass
    test = test_def(args)


if __name__ == '__main__':
    main()
