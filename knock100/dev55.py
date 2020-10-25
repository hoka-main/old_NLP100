import dev52
import dev53
from sklearn.metrics import confusion_matrix


def main():
    Log = dev52.Lg()
    x_train = Log[0][0]
    y_train = Log[0][1]
    train_pred = dev53.pred(x_train, y_train)
    train_cm = confusion_matrix(y_train, train_pred)
    print(train_cm)

    test_pred = dev53.pred(Log[4], Log[5])
    test_cm = confusion_matrix(Log[5], test_pred)
    print(test_cm)


if __name__ == '__main__':
    main()
