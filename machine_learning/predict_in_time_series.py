import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree, svm
from collections import Counter

data_type = "the_day" # one_more_day # the_day

data = pd.read_excel(data_type + ".xlsx")
time_series = pd.read_excel("code600030_small.xlsx")

dv_train = DictVectorizer(sparse=False)  # sparse=False

X = data.drop(["type_is"], axis=1)  # dv_train.fit_transform(data.drop(["type_is"], axis=1))
Y = data["type_is"]

clf = svm.SVC(kernel="rbf", gamma="auto")
clf.fit(X, Y)
r_score = clf.score(X, Y)
print(r_score)

time_series = time_series[["open", "high", "close", "low", "volume", "p_change"]]
result = []
for i in range(len(time_series)):
    one_row = time_series.loc[i]
    result.extend(clf.predict(pd.DataFrame(one_row).T))

print(result)
print(Counter(result))

# one more day
if data_type == "one_more_day":
    result = result[1:]
    result.append("in_trend")

result = pd.Series(result)  # pd.DataFrame(pd.Series(result)).to_excel("predict.xlsx")

from ding_di import *

this_code = "600030"
this_data = pd.read_excel("code" + this_code + "_small.xlsx")
this_data.index = range(len(this_data))
this_functions = {"ding": get_ding, "di": get_di}
this_fun_result = run_functions(this_functions, this_data)

this_fun_result = combine_interval_points(this_fun_result, this_data)

this_linked_result = link_between_ding_di(this_data, this_fun_result)
real_data = merge_result_back_to_data(this_data, this_linked_result, this_fun_result)


def gain_p_type(real, predict):
    if real == predict and real != "in_trend":
        return real + "_tp"
    elif real != "in_trend" and predict == "in_trend":
        return real + "_fn"
    elif real == "in_trend" and predict != "in_trend":
        return real + "_fp"
    return real


real_data["predict"] = result
real_data["ptype"] = real_data.apply(lambda x: gain_p_type(x["ptype"], x["predict"]), axis=1)

real_data = visual(real_data)
# print(this_fun_result[:2])
with open("result.json", mode="w") as a_file:
    a_file.write(real_data)
