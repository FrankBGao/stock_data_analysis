import pandas as pd

data = pd.read_excel("sh60030.xlsx")
data.index = range(len(data))


def get_ding(input_data):
    one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["high"] > two["high"] > three["high"]
    if not cond_1:
        return False
    cond_2 = two["high"] < one["low"] or three["high"] < one["low"]
    if not cond_2:
        return False
    return True


def get_di(input_data):
    one, two, three = input_data  # (input_data[0], input_data[1], input_data[2])
    cond_1 = one["high"] < two["high"] < three["high"]
    if not cond_1:
        return False
    cond_2 = two["low"] > one["high"] or three["low"] > one["high"]
    if not cond_2:
        return False
    return True


functions = {"ding": get_ding, "di": get_di}

result = []
one_slide = 3
for i in range(len(data) - one_slide):
    this_result = []
    for fun_name in functions:
        fun = functions[fun_name]
        the_input_data = [data.loc[i + j] for j in range(one_slide)]
        if fun(the_input_data):
            this_result.append(fun_name)

    if len(this_result) == 0:
        continue
    if len(this_result) == 1:
        result.append({"date": i, "type_is": this_result[0]})
    else:
        result.append({"date": i, "type_is": this_result})

print(result)
