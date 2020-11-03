from sklearn.metrics import accuracy_score
from knock100 import knock52, knock53


def main():
    log = knock52.Lg()
    clf = knock52.load_clf()

    train_pred = knock53.pred(clf, log['train_feature'])
    train_accuracy = accuracy_score(log['train_category'], train_pred)
    print(train_accuracy)

    test_pred = knock53.pred(clf, log['test_feature'])
    test_accuracy = accuracy_score(log['test_category'], test_pred)
    print(test_accuracy)


if __name__ == '__main__':
    main()
