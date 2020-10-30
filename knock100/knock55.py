from sklearn.metrics import confusion_matrix
from knock100 import knock52, knock53




def main():
    log = knock52.Lg()
    feature_train = log[1][0]
    train_category = log[1][1]
    train_pred = knock53.pred(log[0], feature_train)
    train_cm = confusion_matrix(train_category, train_pred)
    print(train_cm)

    feature_test = log[3][0]
    test_category = log[3][1]
    test_pred = knock53.pred(log[0], feature_test)
    test_cm = confusion_matrix(test_category, test_pred)
    print(test_cm)
    breakpoint()


if __name__ == '__main__':
    main()
