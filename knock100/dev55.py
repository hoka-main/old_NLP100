from sklearn.metrics import confusion_matrix
import dev52
import dev53


def main():
    log = dev52.Lg()
    feature_train = log[0][0]
    train_category = log[0][1]
    train_pred = dev53.pred(feature_train, train_category)
    train_cm = confusion_matrix(train_category, train_pred)
    print(train_cm)

    feature_test = log[2][0]
    test_category = log[2][1]
    test_pred = dev53.pred(feature_test, test_category)
    test_cm = confusion_matrix(test_category, test_pred)
    print(test_cm)


if __name__ == '__main__':
    main()
