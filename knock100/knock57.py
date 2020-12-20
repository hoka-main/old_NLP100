from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import knock52


def print_best_and_worst(log, clf):
    features = log['train_feature'].columns.values
    index = [i for i in range(1, 11)]
    for category, coef in zip(clf.classes_, clf.coef_):
        print(f'【カテゴリ】{category}')
        best10 = pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=['重要度トップ10'], index=index).T
        worst10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=['重要度ワースト10'], index=index).T
        print(pd.concat([best10, worst10], axis=0))
        print('\n')


def main():
    log = knock52.Lg()
    clf = knock52.load_clf()
    print_best_and_worst(log, clf)


if __name__ == '__main__':
    main()
