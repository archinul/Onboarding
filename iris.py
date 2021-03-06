import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


def main():
    # import some data to play with
    iris = datasets.load_iris()
    # Take the first two features. We could avoid this by using a two-dim dataset
    X = iris.data[:, :2]
    y = iris.target

    # Logistic regression
    clf = LogisticRegression(multi_class='auto', solver="lbfgs")
    clf.fit(X, y)
    print("predictions:", clf.predict(X))

    scores = cross_val_score(clf, X, y, cv=5, scoring="accuracy")
    return scores


if __name__ == '__main__':
    scores = main()
    print("accuracy:", np.mean(scores))
