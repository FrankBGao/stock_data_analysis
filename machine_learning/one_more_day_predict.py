import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree, svm

from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPClassifier

data = pd.read_excel("one_more_day.xlsx")
# data = pd.read_excel("the_day.xlsx")

dv_train = DictVectorizer(sparse=False)  # sparse=False

test_size = 0.75

X = data.drop(["type_is"], axis=1)  # dv_train.fit_transform(data.drop(["type_is"], axis=1))
Y = dv_train.fit_transform([{"type_is": i} for i in data["type_is"]])
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=test_size)

Y_clf = data["type_is"]
x_train_clf, x_test_clf, y_train_clf, y_test_clf = train_test_split(X, Y_clf, random_state=42, test_size=test_size)


d_tree = tree.DecisionTreeClassifier(criterion="entropy")
d_tree.fit(x_train, y_train)

r_score = d_tree.score(x_train, y_train)
acc_score = d_tree.score(x_test, y_test)

print("dt")
print(r_score)
print(acc_score)

regr = RandomForestRegressor(max_depth=5, random_state=42)
regr.fit(x_train, y_train)

r_score = regr.score(x_train, y_train)
acc_score = regr.score(x_test, y_test)
print("r_dt")
print(r_score)
print(acc_score)

clf = svm.SVC(kernel="rbf", gamma="auto")
clf.fit(x_train_clf, y_train_clf)
r_score = clf.score(x_train_clf, y_train_clf)
acc_score = clf.score(x_test_clf, y_test_clf)
print("svc")
print(r_score)
print(acc_score)


mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10, alpha=1e-4,
                    solver='sgd', verbose=10, random_state=1,
                    learning_rate_init=.1)
mlp.fit(x_train, y_train)
r_score = mlp.score(x_train, y_train)
acc_score = mlp.score(x_test, y_test)
print("nn")
print(r_score)
print(acc_score)
