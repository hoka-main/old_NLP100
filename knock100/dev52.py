from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd


def read_def():
    default_txt_pass = [
        'ch06/train.txt',
        'ch06/valid.txt',
        'ch06/test.txt'
    ]
    return_file = []
    for file in default_txt_pass:
        text = pd.read_csv(file, sep='\t', names=['TITLE', 'CATEGORY'])
        category = text.CATEGORY
        return_file.append(category)
    return return_file


def main():
    feature_txt_pass = [
        'ch06/train.feature.txt',
        'ch06/valid.feature.txt',
        'ch06/test.feature.txt'
    ]

    x_id = []
    for file in feature_txt_pass:
        with open(file) as file_x_id:
            x_id.append(file_x_id.read())
    train_x = x_id[2]
    dataframe_list = read_def()
    train = dataframe_list[2]
    # valid = dataframe_list[1]
    # test = dataframe_list[2]

    lg = LogisticRegression(random_state=123, max_iter=10000)
    lg.fit(train_x, train)


if __name__ == '__main__':
    main()
