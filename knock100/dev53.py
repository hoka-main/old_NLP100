from sklearn.linear_model import LogisticRegression
import pandas as pd
from knock100 import dev52


def pred(clf, wanna_pred_feature_table):
    to_pred = clf.predict(wanna_pred_feature_table)
    return to_pred


def main():
    log = dev52.Lg()
    feature_train = log[1][0]
    print(pred(log[0], feature_train))


if __name__ == '__main__':
    main()
