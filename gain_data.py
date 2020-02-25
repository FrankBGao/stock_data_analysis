import tushare as ts
import copy


def gain_data(code):
    """

    :param code: stock code # 600030
    :return: pd.DataFrame
    """
    data = ts.get_hist_data(code)  # 一次性获取全部日k线数据
    data["date"] = copy.deepcopy(data.index)#[i for i in data.index]
    data.index = range(len(data))
    data = data.sort_values("date")
    data.index = range(len(data))
    return data


print(gain_data("600030"))
