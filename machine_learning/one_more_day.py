import pandas as pd
from ding_di import run_functions, get_ding, get_di
from machine_learning.predict_ding_di import combine_interval_points, gain_training_set, gain_random_no_meaning_point, \
    a_point_after_ding_di, the_point_at_ding_di


def gain_one_more_day_data(fun_result, data):
    fun_result = combine_interval_points(fun_result, data)
    training_set = gain_training_set(fun_result, data)
    no_meaning_point = gain_random_no_meaning_point(fun_result, data, len(fun_result) * 3)
    points_after_ding_di = a_point_after_ding_di(training_set, one_type=False)
    training_set = no_meaning_point.append(points_after_ding_di)
    training_set.index = range(len(training_set))
    return training_set


def gain_one_day_data(fun_result, data):
    fun_result = combine_interval_points(fun_result, data)
    training_set = gain_training_set(fun_result, data)
    no_meaning_point = gain_random_no_meaning_point(fun_result, data, len(fun_result) * 3)
    points_after_ding_di = the_point_at_ding_di(training_set, one_type=False)
    training_set = no_meaning_point.append(points_after_ding_di)
    training_set.index = range(len(training_set))
    return training_set


this_code = "600030"  # 600036 # 600298 # 000858
this_functions = {"ding": get_ding, "di": get_di}
this_data = pd.read_excel("code" + this_code + ".xlsx")
this_data.index = range(len(this_data))
this_fun_result = run_functions(this_functions, this_data)
this_training_data = gain_one_more_day_data(this_fun_result, this_data)

this_training_data.to_excel("one_more_day.xlsx", index=False)
#print(this_training_data)

this_training_data = gain_one_day_data(this_fun_result, this_data)
this_training_data.to_excel("the_day.xlsx", index=False)