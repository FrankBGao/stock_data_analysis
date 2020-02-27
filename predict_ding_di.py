import pandas as pd


def combine_interval_points(fun_result, data):
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
        target_item = price_fun(price)
        target_index = price.index(target_item)
        target = comb[target_index]
        new_list.append(target)
    return new_list


if __name__ == '__main__':
    from ding_di import run_functions, get_ding, get_di

    this_code = "600030"  # 600036 # 600298 # 000858

    this_functions = {"ding": get_ding, "di": get_di}
    this_data = pd.read_excel("code" + this_code + ".xlsx")
    this_data.index = range(len(this_data))
    this_fun_result = run_functions(this_functions, this_data)
    # print(this_fun_result)
    a = combine_interval_points(this_fun_result, this_data)

    print(a)
