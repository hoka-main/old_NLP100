from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import dev52


def main():
    log = dev52.Lg()
    feature_train = log[0][0]
    train_category = log[0][1]
    clf = LogisticRegression(random_state=123, max_iter=10000)
    clf.fit(feature_train, train_category)
    features = feature_train.columns.values
    index = [i for i in range(1, 11)]
    for category, coef in zip(clf.classes_, clf.coef_):
        print(f'【カテゴリ】{category}')
        best10 = pd.DataFrame(features[np.argsort(coef)[::-1][:10]], columns=['重要度トップ10'], index=index).T
        worst10 = pd.DataFrame(features[np.argsort(coef)[:10]], columns=['重要度ワースト10'], index=index).T
        print(pd.concat([best10, worst10], axis=0))
        print('\n')


if __name__ == '__main__':
    main()
