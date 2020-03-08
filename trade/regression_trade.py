from ding_di import *
from trade.Trader import Trader
from trade.strategy import *
import pandas as pd
import json
from data_interface.data_interface import gain_code_data_excel


def run_functions(functions, data):
    result = []
    for fun_name in functions:
        fun = functions[fun_name]
        if fun(data):
            result.append(fun_name)

    return result


def regress_trading(function_dict, data, trader, stock_code, buy_switches=None):
    """

    :param function_dict:
    :param data:
    :param trader:
    :param stock_code:
    :param buy_switches: {"2019-2-2":true}
    :return:
    """
    data.index = range(len(data))
    max_one_slide = max([function_dict[i]["sliding_window"] for i in function_dict])

    everyday_results = []
    buy_switch = True
    for i in range(max_one_slide, len(data)):
        # buy_switch for turn on or turn off, according with the date
        if not buy_switches is None:
            if data.iloc[i]["date"] in buy_switches:
                buy_switch = buy_switches[data.iloc[i]["date"]]

        ding_di = []
        for fun_name in function_dict:
            fun = function_dict[fun_name]["fun"]
            one_slide = function_dict[fun_name]["sliding_window"]

            inter_data = data.loc[i - one_slide: i]
            inter_data = [inter_data.iloc[j] for j in range(one_slide)]

            if fun(inter_data):
                ding_di.append(fun_name)

        stock_info = {
            "stock": stock_code,
            "price": data.iloc[i]["close"],
            "date": data.iloc[i]["date"]
        }
        # trader = dummy_strategy(ding_di, trader, stock_info)
        # trader = naive_trading_strategy(ding_di, trader, stock_info, buy_switch = buy_switch,)
        # trader = naive_w_cold_down(ding_di, trader, stock_info, cold_down_period="30 day")
        # trader = earn_percent_trading_strategy(ding_di, trader, stock_info, 0.05)
        # trader = earn_percent_w_smart_start(ding_di, trader, stock_info, 0.05)
        # trader = earn_percent_w_smart_start_w_small_steps(ding_di, trader, stock_info, 0.05)
        # trader = earn_percent_trading_strategy_with_safety(ding_di, trader, stock_info, 0.05, 0.1)
        # trader = earn_percent_w_safety_w_smart_start(ding_di, trader, stock_info, 0.05, 0.2)
        # trader = earn_percent_w_smart_start_w_small_steps_w_safety(ding_di, trader, stock_info, 0.05, 0.1,
        #                                                            cold_down_period="45 day")
        trader = earn_percent_w_smart_start_w_small_steps_w_safety_double(ding_di, trader, stock_info,
                                                                          up_threshold=0.10,
                                                                          down_threshold=0.03,
                                                                          safety_down=0.2,
                                                                          safety_up=0.1,
                                                                          buy_switch=buy_switch,
                                                                          initial_step="normal",  # sensitive
                                                                          cold_down_period=str(30) + " day")

        inter = trader.gain_result({stock_code: data.iloc[i]["close"]})
        inter["date"] = data.iloc[i]["date"]
        inter["stock"] = stock_code
        everyday_results.append(inter)

    stock_info = {
        stock_code: data.loc[len(data) - 1]["close"]
    }
    # print(trader.gain_result(stock_info))

    return trader, trader.gain_result(stock_info), everyday_results


def regress_trading_product(function_dict, data, trader, stock_code, buy_switches=None, parameter=None,
                            strategy="complex"):
    """
    :param function_dict:
    :param data:
    :param trader:
    :param stock_code:
    :param buy_switches: {"2019-2-2":true}
    :param parameter: {}
    :param strategy: complex, naive
    :return:
    """
    data.index = range(len(data))
    max_one_slide = max([function_dict[i]["sliding_window"] for i in function_dict])

    everyday_results = []
    buy_switch = True

    ding_di_result = []
    for i in range(max_one_slide - 1, len(data)):
        # buy_switch for turn on or turn off, according with the date
        if not buy_switches is None:
            if data.iloc[i]["date"] in buy_switches:
                buy_switch = buy_switches[data.iloc[i]["date"]]

        ding_di = []
        for fun_name in function_dict:
            fun = function_dict[fun_name]["fun"]
            one_slide = function_dict[fun_name]["sliding_window"]

            inter_data = data.loc[i - one_slide: i]
            inter_data = [inter_data.iloc[j] for j in range(one_slide)]

            if fun(inter_data):
                ding_di.append(fun_name)
        if len(ding_di) > 0:
            ding_di_result.append({"index": i, "type_is": ding_di[0]})

        stock_info = {
            "stock": stock_code,
            "price": data.iloc[i]["close"],
            "date": data.iloc[i]["date"]
        }

        if strategy == "complex":
            trader = earn_percent_w_smart_start_w_small_steps_w_safety_double(ding_di, trader, stock_info,
                                                                              up_threshold=parameter["up_threshold"],
                                                                              down_threshold=parameter[
                                                                                  "down_threshold"],
                                                                              safety_down=parameter["safety_down"],
                                                                              safety_up=parameter["safety_up"],
                                                                              initial_step=parameter["initial_step"],
                                                                              # sensitive
                                                                              cold_down_period=str(
                                                                                  parameter[
                                                                                      "cold_down_period"]) + " day")
        elif strategy == "naive":
            trader = naive_trading_strategy(ding_di, trader, stock_info, buy_switch=buy_switch)
        else:
            trader = naive_trading_strategy(ding_di, trader, stock_info, buy_switch=buy_switch)

        inter = trader.gain_result({stock_code: data.iloc[i]["close"]})
        inter["date"] = data.iloc[i]["date"]
        inter["stock"] = stock_code
        everyday_results.append(inter)

    stock_info = {
        stock_code: data.loc[len(data) - 1]["close"]
    }

    return trader, trader.gain_result(stock_info), everyday_results, ding_di_result


def buy_switch_generator(data):
    switch = {
        "on": True,
        "off": False
    }
    result = {}
    for i in range(len(data)):
        result[data.iloc[i]["date"]] = switch[data.iloc[i]["switch"]]
    return result


# product
def gain_p_type(ptype, type_is):
    result = []
    for pt, buy_sell in zip(ptype, type_is):
        if pd.isna(buy_sell):
            result.append(pt)
        else:
            if pt == "in_trend":
                result.append(buy_sell)
            else:
                result.append(pt + "_" + buy_sell)
    return result


def producing_ding_di(data, fun_result, combine_switch):
    if combine_switch:
        fun_result = combine_interval_points(fun_result, data, just_first_one=True)

    linked_result = link_between_ding_di(data, fun_result)
    result = merge_result_back_to_data(data, linked_result, fun_result)
    # result = visual(result)
    return result.drop(["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis=1)


def run_regression(code, invest, parameter=None, combine_switch=True, strategy="complex"):

    # data = pd.read_excel("data/code" + code + ".xlsx")
    # calling from the app
    # try:
    #     data = pd.read_excel("trade/data/code" + code + ".xlsx")
    # except FileNotFoundError:
    #     to_download_data_path(code, "trade/data/")
    #     data = pd.read_excel("trade/data/code" + code + ".xlsx")

    # buy_switch = pd.DataFrame([{"date": "2017-09-15", "switch": "off"}, {"date": "2019-01-11", "switch": "on"}])
    # buy_switch.to_excel("buy_switch.xlsx")
    # buy_switch = buy_switch_generator(buy_switch)

    data = gain_code_data_excel(code)

    functions = {"ding": {"fun": get_ding, "sliding_window": 3}, "di": {"fun": get_di, "sliding_window": 3}}
    the_trader = Trader(invest)
    the_trader, the_result, the_everyday_result, ding_di_result = regress_trading_product(functions, data, the_trader,
                                                                                          code,
                                                                                          parameter=parameter,
                                                                                          strategy=strategy
                                                                                          )
    trading_record = pd.DataFrame(the_trader.trading_record)
    trading_record_table = trading_record.copy()
    trading_record = trading_record[["quantity", "type_is", "date", "option"]]
    the_everyday_result = pd.DataFrame(the_everyday_result)
    the_everyday_result = pd.merge(the_everyday_result, trading_record, on="date", how="left")

    # ding di visual
    ding_di_result = producing_ding_di(data, ding_di_result, combine_switch)
    the_everyday_result = pd.merge(ding_di_result, the_everyday_result, on="date", how="left")
    the_everyday_result["ptype"] = gain_p_type(the_everyday_result["ptype"], the_everyday_result["type_is"])
    the_everyday_result = the_everyday_result.rename(axis="columns",
                                                     mapper={"date": "time", "open": "start", "close": "end",
                                                             "high": "max", "low": "min",
                                                             "volume": "volumn"})
    the_everyday_result["money"] = the_everyday_result["start"] * the_everyday_result["volumn"]
    the_everyday_result["type_is"] = the_everyday_result["type_is"].fillna("Hold")
    # the_everyday_result.to_json("regress.json", orient="records")
    # trading_record_table.to_json("trading_record.json", orient="records")
    # json.dump(the_result, open("regress_result.json",mode = "w"))
    return {"result": the_result, "everyday_result": the_everyday_result.to_json(orient="records"),
            "trading_record": trading_record_table.to_json(orient="records")}


if __name__ == '__main__':
    this_code = "600030"  # 600036 # 600298 # 000858 # 000725 # 600999 # 600030
    this_data = pd.read_excel("data/code" + this_code + ".xlsx")
    this_functions = {"ding": {"fun": get_ding, "sliding_window": 3}, "di": {"fun": get_di, "sliding_window": 3}}
    a_trader = Trader(100000)

    # this_buy_switch = pd.DataFrame([{"date": "2017-09-15", "switch": "off"}, {"date": "2019-01-11", "switch": "on"}])
    # this_buy_switch.to_excel("buy_switch.xlsx")
    # this_buy_switch = buy_switch_generator(this_buy_switch)

    # a_trader, a_result, a_everyday_result = regress_trading(this_functions, this_data, a_trader, this_code,
    #                                                         this_buy_switch)
    a_trader, a_result, a_everyday_result = regress_trading(this_functions, this_data, a_trader, this_code)
    a = a_trader.trading_record
    a = pd.DataFrame(a)
    print(a_result)
    print(a)
    print(a_everyday_result)
    a.to_excel(this_code + "回测结果.xlsx", index=False)

    # this_parameter = {
    #     "up_threshold": 0.05,
    #     "down_threshold": 0.1,
    #     "safety_down": 0.2,
    #     "safety_up": 0.1,
    #     "initial_step": "normal",
    #     "cold_down_period": 30,
    # }
    # a = run_regression(this_code, 100000, this_parameter)
    # print(a)

    # trading_record = trading_record[["price","quantity","amount","type_is","date","option","all_money"]]
    # {"result": the_result, "trading_record": the_trader.trading_record, "everyday_result": the_everyday_result}

# up_threshold = parameter["up_threshold"],
# down_threshold = parameter[
#                      "down_threshold"],
# safety_down = parameter["safety_down"],
# safety_up = parameter["safety_up"],
# initial_step = parameter["initial_step"],
# # sensitive
# cold_down_period = str(
#     parameter[
#         "cold_down_period"]) + " day")
