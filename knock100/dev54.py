from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import dev52
import dev53


def main():
    Log = dev52.Lg()
    x_train = Log[0]
    y_train = Log[1]
    x_test = Log[4]
    y_test = Log[5]

    train_pred = dev53.pred(x_train, y_train)
    test_pred = dev53.pred(x_test, y_test)

    train_accuracy = accuracy_score(y_train, train_pred)
    test_accuracy = accuracy_score(y_test, test_pred)
    print(train_accuracy)
    print(test_accuracy)


if __name__ == '__main__':
    main()
