from knock100 import knock52, knock53, knock58
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from tqdm import tqdm
import numpy as np


def over_fitting(log):
    result = []
    for C in tqdm(np.logspace(-4, 1, 6)):

        clf = LogisticRegression(random_state=123,
                                 max_iter=10000,
                                 solver='liblinear',
                                 tol=1e-5,
                                 C=C
                                 )
        clf.fit(log['train_feature'], log['train_category'])
        train_pred = knock53.pred(clf, log['train_feature'])
        valid_pred = knock53.pred(clf, log['valid_feature'])
        test_pred = knock53.pred(clf, log['test_feature'])

        train_accuracy = accuracy_score(log['train_category'], train_pred)
        valid_accuracy = accuracy_score(log['valid_category'], valid_pred)
        test_accuracy = accuracy_score(log['test_category'], test_pred)

        result.append([C, train_accuracy, valid_accuracy, test_accuracy])

    result = np.array(result).T
    return result


def main():
    log = knock52.Lg()
    result = over_fitting(log)
    knock58.plot(result)


if __name__ == '__main__':
    main()

# trainで学習
# testでパラメータチューニング
# validでチューニング後のモデルを復習
