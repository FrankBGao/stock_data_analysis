import pandas as pd
import copy
import random


def combine_interval_points(fun_result, data, just_first_one=False):
    # combine
    need_combine = []
    inter = []
    len_fun_result = len(fun_result)
    for index, i in enumerate(fun_result[:-1]):
        if fun_result[index + 1]["type_is"] == i["type_is"]:
            if i not in inter:
                inter.append(i)
            inter.append(fun_result[index + 1])

            # check the last one
            if index == len_fun_result - 2:
                need_combine.append(inter)
        else:
            if len(inter) != 0:
                need_combine.append(inter)
                inter = []
            else:
                need_combine.append(i)
            # check the last one
            if index == len_fun_result - 2:
                if fun_result[index + 1] not in need_combine[:-1]:
                    need_combine.append(fun_result[index + 1])

    # replace
    new_list = []
    for comb in need_combine:
        if not isinstance(comb, list):
            new_list.append(comb)
            continue
        # if comb[0]["index"] == 576:
        #     pass
        type_is = comb[0]["type_is"]
        if type_is == "di":
            price_type = "low"
            price_fun = min
        else:
            price_type = "high"
            price_fun = max

        price = []
        for i in comb:
            price.append(data.loc[i["index"]][price_type])
        if not just_first_one:
            target_item = price_fun(price)
            target_index = price.index(target_item)
        else:
            target_index = 0

        target = comb[target_index]
        new_list.append(target)
    return new_list


#######################################################################################################################
#  gain training data #################################################################################################
#######################################################################################################################


def gain_training_set(fun_result, data, set_len=5):
    """

    :param fun_result: the ding di result
    :param data: whole dataFrame
    :param set_len: how many data point you want to use to predict
    :return: a list of data for which ding di
    """
    in_function_data = data[["open", "high", "close", "low", "volume", "p_change"]]

    training_set = []
    for i in fun_result:
        index = i["index"]
        if index < set_len:
            continue
        inter_data = in_function_data.loc[index - set_len + 1:index]

        training_set.append({"point": i,
                             "point_information": copy.deepcopy(in_function_data.loc[index]),
                             "pre_training_data": copy.deepcopy(inter_data),
                             "pro_training_data": copy.deepcopy(in_function_data.loc[index + 1]),
                             })

    return training_set


# training with one step after


def gain_random_no_meaning_point(fun_result, data, len_fun_result=None):
    """
    gain some data point which is not bing and di
    :param fun_result:
    :param data:
    :param len_fun_result:
    :return:
    """
    if len_fun_result is None:
        len_fun_result = len(fun_result) * 2

    ding_di_result = [i["index"] for i in fun_result]

    all_index = set(range(len(data)))

    no_meaning_point = all_index.difference(set(ding_di_result))
    no_meaning_point = list(no_meaning_point)
    no_meaning_point = random.sample(no_meaning_point, len_fun_result)
    no_meaning_point.sort()

    no_meaning_point = copy.deepcopy(data.loc[no_meaning_point])
    no_meaning_point["type_is"] = "in_trend"
    no_meaning_point = no_meaning_point[["open", "high", "close", "low", "volume", "p_change", "type_is"]]
    return no_meaning_point


def a_point_after_ding_di(training_set, one_type=True):
    result = pd.DataFrame()
    for i in training_set:
        inter = copy.deepcopy(i["pro_training_data"])
        inter["type_is"] = i["point"]["type_is"]
        result = result.append(inter)
    if one_type:
        result["type_is"] = "ding_di"
    result = result[["open", "high", "close", "low", "volume", "p_change", "type_is"]]
    return result


def the_point_at_ding_di(training_set, one_type=True):
    result = pd.DataFrame()
    for i in training_set:
        inter = copy.deepcopy(i["point_information"])
        inter["type_is"] = i["point"]["type_is"]
        result = result.append(inter)
    if one_type:
        result["type_is"] = "ding_di"
    result = result[["open", "high", "close", "low", "volume", "p_change", "type_is"]]
    return result


if __name__ == '__main__':
    from ding_di import run_functions, get_ding, get_di

    this_code = "600030"  # 600036 # 600298 # 000858

    this_functions = {"ding": get_ding, "di": get_di}
    this_data = pd.read_excel("code" + this_code + ".xlsx")
    this_data.index = range(len(this_data))
    this_fun_result = run_functions(this_functions, this_data)
    # print(this_fun_result)
    this_fun_result = combine_interval_points(this_fun_result, this_data)
    this_training_set = gain_training_set(this_fun_result, this_data)
    this_no_meaning_point = gain_random_no_meaning_point(this_fun_result, this_data)
    this_points_after_ding_di = a_point_after_ding_di(this_training_set)
    # print(a)

    this_training_set = this_no_meaning_point.append(this_points_after_ding_di)
    print(this_training_set)
