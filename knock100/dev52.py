from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sys
import dev51
import pandas as pd


def read_def(args):
    return_file = []
    del args[0]
    for file in args:
        text = pd.read_csv(file, sep='\t', names=['TITLE', 'CATEGORY'])
        title = text.CATEGORY
        return_file.append(title)
    return return_file


def main():
    args = sys.argv
    feature_txt_pass = [
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
    ]
    default_txt_pass = [
        'ch06/train.txt',
        'ch06/valid.txt',
        'ch06/test.txt'
    ]
    x_id = []
    for file in feature_txt_pass:
        with open(file[0]) as file_x_id:
            x_id.append(file_x_id.read())

    dataframe_list = read_def(default_txt_pass)
    train = dataframe_list[0]
    valid = dataframe_list[1]
    test = dataframe_list[2]
    lg = LogisticRegression(random_state=123, max_iter=10000)
    lg.fit(train_x, train['CATEGORY'])


if __name__ == '__main__':
    main()
