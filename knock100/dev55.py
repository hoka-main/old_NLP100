import dev52
import dev53
from sklearn.metrics import confusion_matrix


def main():
    Log = dev52.Lg()
    x_train = Log[0]
    y_train = Log[1]
    train_pred = dev53.pred(x_train, y_train)
    train_cm = confusion_matrix(y_train, train_pred)
    print(train_cm)


if __name__ == '__main__':
    main()
