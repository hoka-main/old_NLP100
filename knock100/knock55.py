from sklearn.metrics import confusion_matrix
import knock52
import knock53


def main():
    log = knock52.Lg()
    clf = knock52.load_clf()

    train_pred = knock53.pred(clf, log['train_feature'])
    train_cm = confusion_matrix(log['train_category'], train_pred)
    print(train_cm)

    test_pred = knock53.pred(clf, log['test_feature'])
    test_cm = confusion_matrix(log['test_category'], test_pred)
    print(test_cm)


if __name__ == '__main__':
    main()
