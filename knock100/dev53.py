from sklearn.linear_model import LogisticRegression
import pandas as pd
import dev52


def pred(feature_table, default_category):
    clf = LogisticRegression(random_state=123, max_iter=10000)
    clf.fit(feature_table, default_category)
    to_pred = clf.predict(feature_table)
    return to_pred


def main():
    log = dev52.Lg()
    feature_train = log[0][0]
    train_category = log[0][1]
    print(pred(feature_train, train_category))


if __name__ == '__main__':
    main()
