from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import dev52


def pred(x, y):
    clf = LogisticRegression(random_state=123, max_iter=10000)
    clf.fit(x, y)
    to_pred = clf.predict(x)
    return to_pred


def main():
    Log = dev52.Lg()
    x_train = Log[0][0]
    y_train = Log[0][1]
    print(pred(x_train, y_train))


if __name__ == '__main__':
    main()
