from sklearn.linear_model import LogisticRegression
import pandas as pd
import knock52
import pickle


def pred(clf, wanna_pred_feature_table):
    to_pred = clf.predict(wanna_pred_feature_table)
    return to_pred


def main():
    log = knock52.Lg()
    clf = knock52.load_clf()
    print(pred(clf, log['train_feature']))


if __name__ == '__main__':
    main()
