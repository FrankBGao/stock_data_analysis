import pandas as pd
from visual import visual
from gain_data import to_download_data_path
from machine_learning.predict_ding_di import combine_interval_points


# just two days
# def get_ding(input_data):
#     one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
#     cond_1 = one["high"] > two["high"]
#     if not cond_1:
#         return False
#     cond_2 = two["high"] < one["low"]
#     if not cond_2:
#         return False
#     return True
#
#
# def get_di(input_data):
#     one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
#     cond_1 = one["high"] < two["high"]
#     if not cond_1:
#         return False
#     cond_2 = two["low"] > one["high"]
#     if not cond_2:
#         return False
#     return True


def get_ding(input_data):
    # sliding_window = 3
    one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["high"] > two["high"] > three["high"]
    # cond_1 = one["low"] > two["low"] > three["low"]
    if not cond_1:
        return False
    cond_2 = two["high"] < one["low"] or three["high"] < one["low"]
    if not cond_2:
        return False
    return True


def get_di(input_data):
    # sliding_window = 4
    one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["low"] < two["low"] < three["low"]
    # cond_1 = one["high"] < two["high"] < three["high"]
    if not cond_1:
        return False
    cond_2 = two["low"] > one["high"] or three["low"] > one["high"]
    if not cond_2:
        return False
    return True


def get_ding_v2(input_data):
    # sliding_window = 3
    one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = two["high"] > one["high"] and two["high"] > three["high"]
    # cond_1 = one["low"] > two["low"] > three["low"]
    if not cond_1:
        return False
    cond_2 = two["low"] > one["low"] and two["low"] > three["low"]
    if not cond_2:
        return False
    return True


def get_di_v2(input_data):
    # sliding_window = 3
    one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = two["low"] < one["low"] and two["low"] < three["low"]
    # cond_1 = one["high"] < two["high"] < three["high"]
    if not cond_1:
        return False
    cond_2 = two["high"] < one["high"] and two["high"] < three["high"]
    if not cond_2:
        return False
    return True


def get_ding_four(input_data):
    # sliding_window = 3
    one, two, three, four = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["high"] > two["high"] > three["high"] > four["high"]
    if not cond_1:
        return False
    cond_2 = two["high"] < one["low"] or three["high"] < one["low"] or four["high"] < one["low"]
    if not cond_2:
        return False
    return True


def get_di_four(input_data):
    # sliding_window = 4
    one, two, three, four = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["low"] < two["low"] < three["low"] < four["low"]
    if not cond_1:
        return False
    cond_2 = two["low"] > one["high"] or three["low"] > one["high"] or four["low"] > one["high"]
    if not cond_2:
        return False
    return True


def get_ding_five(input_data):
    # sliding_window = 3
    one, two, three, four, five = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["high"] > two["high"] > three["high"] > four["high"] > five["high"]
    if not cond_1:
        return False
    cond_2 = two["high"] < one["low"] or three["high"] < one["low"] or four["high"] < one["low"] or five["high"] < one[
        "low"]
    if not cond_2:
        return False
    return True


def get_di_five(input_data):
    # sliding_window = 4
    one, two, three, four, five = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["low"] < two["low"] < three["low"] < four["low"] < five["low"]
    if not cond_1:
        return False
    cond_2 = two["low"] > one["high"] or three["low"] > one["high"] or four["low"] > one["high"] or five["low"] > one[
        "high"]
    if not cond_2:
        return False
    return True


def get_advance_ding(input_data):
    one, two, three, four = input_data
    cond_1 = two["high"] > three["high"] and one["high"] < two["high"]
    if not cond_1:
        return False
    cond_2 = one["low"] > two["low"] and one["low"] > three["low"]
    if not cond_2:
        return False

    cond_3 = two["high"] > three["high"] > four["high"]
    if not cond_3:
        return False

    cond_4 = two["low"] > three["low"] > four["low"]
    if not cond_4:
        return False

    cond_5 = one["high"] < three["high"] and one["high"] < four["high"]
    if not cond_5:
        return False

    return True


def get_advance_di(input_data):
    one, two, three, four = input_data
    cond_1 = two["low"] < three["low"] and two["low"] < one["low"]
    if not cond_1:
        return False

    cond_2 = one["high"] < two["high"] and one["high"] < three["high"]
    if not cond_2:
        return False

    cond_3 = two["high"] < three["high"] < four["high"]
    if not cond_3:
        return False

    cond_4 = two["low"] < three["low"] < four["low"]
    if not cond_4:
        return False

    cond_5 = one["low"] > three["low"] and one["low"] > four["low"]
    if not cond_5:
        return False

    return True


def run_functions(functions, data):
    data.index = range(len(data))
    result = []
    max_one_slide = max([functions[i]["sliding_window"] for i in functions])
    for i in range(len(data) - max_one_slide + 1):
        this_result = []
        for fun_name in functions:
            fun = functions[fun_name]["fun"]
            one_slide = functions[fun_name]["sliding_window"]
            the_input_data = [data.loc[i + j] for j in range(one_slide)]
            if fun(the_input_data):
                this_result.append(fun_name)

        if len(this_result) == 0:
            continue

        # 纠正过滞后的
        # if len(this_result) == 1:
        #     result.append({"index": i + one_slide - 1, "type_is": this_result[0]})
        # else:
        #     result.append({"index": i + one_slide - 1, "type_is": this_result})
        if len(this_result) == 1:
            result.append({"index": i, "type_is": this_result[0]})
        else:
            result.append({"index": i, "type_is": this_result})

    return result


#######################################################################################################################
#  make it pretty     #################################################################################################
#######################################################################################################################


def link_between_ding_di(data, fun_result):
    if len(fun_result) == 0:
        return []
    result = []
    for index in range(len(fun_result) - 1):
        source_index = fun_result[index]["index"]
        target_index = fun_result[index + 1]["index"]

        date_interval = target_index - source_index

        source = data.loc[source_index]
        target = data.loc[target_index]

        price_interval = target["open"] - source["open"]

        delta = price_interval / date_interval

        inter_result = []
        for small_index in range(date_interval):
            inter = {
                "point": source["open"] + delta * small_index,
                "index": small_index + source_index
            }
            inter_result.append(inter)

        result.extend(inter_result)
    return result


def merge_result_back_to_data(data, linked_result, fun_result):
    if len(fun_result) == 0:
        data["point"] = data["open"]
        data["ptype"] = "in_trend"
        return data

    linked_result = pd.DataFrame(linked_result)
    linked_result.index = linked_result["index"]

    fun_result = pd.DataFrame(fun_result)
    fun_result.index = fun_result["index"]

    data["point"] = linked_result["point"]
    data["ptype"] = fun_result["type_is"]

    # min_open = data["open"].min()
    # data.apply(lambda x: x["open"] if x["point"] == np.nan else x["point"], axis=1)
    # data.apply(lambda x: x["open"] if x["point"] != np.nan else x["point"], axis=1)
    data["point"] = data.apply(lambda x: x["open"] if pd.isna(x["point"]) else x["point"], axis=1)
    data["ptype"] = data["ptype"].fillna("in_trend")
    return data


if __name__ == '__main__':
    this_functions = {"ding": {"fun": get_ding, "sliding_window": 3}, "di": {"fun": get_di, "sliding_window": 3}}
    # this_functions = {"ding": {"fun": get_ding_v2, "sliding_window": 3}, "di": {"fun": get_di_v2, "sliding_window": 3}}
    # this_functions = {"ding": {"fun": get_advance_ding, "sliding_window": 4},
    #                   "di": {"fun": get_advance_di, "sliding_window": 4}}
    # this_functions = {"ding": {"fun": get_ding_four, "sliding_window": 4},
    #                   "di": {"fun": get_di_four, "sliding_window": 4}}
    # this_functions = {"ding": {"fun": get_ding_five, "sliding_window": 5},
    #                   "di": {"fun": get_di_five, "sliding_window": 5}}
    # this_data = pd.read_excel("sh60030.xlsx")
    this_code = "000596"  # 600036 # 600298 # 000858 # 600999 # 000527 # 600717 # 600030

    try:
        this_data = pd.read_excel("trade/data/code" + this_code + ".xlsx")
    except FileNotFoundError:
        to_download_data_path(this_code, "trade/data/")
        this_data = pd.read_excel("trade/data/code" + this_code + ".xlsx")

    this_data.index = range(len(this_data))
    this_fun_result = run_functions(this_functions, this_data)

    this_fun_result = combine_interval_points(this_fun_result, this_data, just_first_one=True)

    this_linked_result = link_between_ding_di(this_data, this_fun_result)
    a = merge_result_back_to_data(this_data, this_linked_result, this_fun_result)
    # a.to_excel("result" + this_code + ".xlsx")
    a = visual(a)
    # print(this_fun_result[:2])
    with open("result.json", mode="w") as a_file:
        a_file.write(a)
    # print(a)

    # begin = data["open"].loc[:linked_result["index"].iloc[0]]
    # inter = list(begin)
    # inter2 = list(linked_result["point"])
    # inter.extend(inter2)
    # data["point"] = inter
