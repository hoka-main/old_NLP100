from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import dev52


def main():
    train = dev52.Lg()
    x_train = train[0]
    y_train = train[1]
    clf = LogisticRegression(random_state=123, max_iter=10000)
    clf.fit(x_train, y_train)
    train_pred = clf.predict(x_train)
    print(train_pred)


if __name__ == '__main__':
    main()
