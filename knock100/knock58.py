from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from tqdm import tqdm
from knock100 import knock52, knock53
import numpy as np


def main():
    log = knock52.Lg()
    clf = log[0]
    feature_train = log[1][0]
    train_category = log[1][1]
    feature_valid = log[2][0]
    valid_category = log[2][1]
    feature_test = log[3][0]
    test_category = log[3][1]
    result = []

    for C in tqdm(np.logspace(-2, 1, 10)):

        clf = LogisticRegression(random_state=123, max_iter=10000, C=C)
        clf.fit(feature_train, train_category)

        train_pred = knock53.pred(clf, feature_train)
        valid_pred = knock53.pred(clf, feature_valid)
        test_pred = knock53.pred(clf, feature_test)

        train_accuracy = accuracy_score(train_category, train_pred)
        valid_accuracy = accuracy_score(valid_category, valid_pred)
        test_accuracy = accuracy_score(test_category, test_pred)

        result.append([C, train_accuracy, valid_accuracy, test_accuracy])

    result = np.array(result).T

    plt.plot(result[0], result[1], label='train')
    plt.plot(result[0], result[2], label='valid')
    plt.plot(result[0], result[3], label='test')
    plt.ylim(0, 1.1)
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.xlabel('C')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
