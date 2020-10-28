from sklearn.metrics import accuracy_score
import dev52
import dev53


def main():
    log = dev52.Lg()
    feature_train = log[0][0]
    train_category = log[0][1]
    feature_test = log[2][0]
    test_category = log[2][1]

    train_pred = dev53.pred(feature_train, train_category)
    test_pred = dev53.pred(feature_test, test_category)

    train_accuracy = accuracy_score(train_category, train_pred)
    test_accuracy = accuracy_score(test_category, test_pred)
    print(train_accuracy)
    print(test_accuracy)


if __name__ == '__main__':
    main()
