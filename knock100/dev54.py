from sklearn.metrics import accuracy_score
from knock100 import dev52, dev53


def main():
    log = dev52.Lg()
    feature_train = log[1][0]
    feature_test = log[3][0]
    train_category = log[1][1]
    test_category = log[3][1]

    train_pred = dev53.pred(log[0], feature_train)
    test_pred = dev53.pred(log[0], feature_test)

    train_accuracy = accuracy_score(train_category, train_pred)
    test_accuracy = accuracy_score(test_category, test_pred)
    print(train_accuracy)
    print(test_accuracy)


if __name__ == '__main__':
    main()
