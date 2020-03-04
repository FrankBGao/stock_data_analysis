from ding_di import *
from trade.Trader import Trader
from trade.strategy import *


def run_functions(functions, data):
    result = []
    for fun_name in functions:
        fun = functions[fun_name]
        if fun(data):
            result.append(fun_name)

    return result


def regress_trading(function_dict, data, trader, stock_code, buy_switches = dict()):
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
                                                                          up_threshold=0.05,
                                                                          down_threshold=0.1,
                                                                          safety_down=0.2,
                                                                          safety_up=0.1,
                                                                          buy_switch=buy_switch,
                                                                          initial_step="normal",  # sensitive
                                                                          cold_down_period="30 day")

        inter = trader.gain_result({stock_code: data.iloc[i]["close"]})
        inter["date"] = data.iloc[i]["date"]
        inter["stock"] = stock_code
        everyday_results.append(inter)

    stock_info = {
        stock_code: data.loc[len(data) - 1]["close"]
    }
    # print(trader.gain_result(stock_info))

    return trader, trader.gain_result(stock_info), everyday_results


def buy_switch_generator(data):
    switch = {
        "on": True,
        "off": False
    }
    result = {}
    for i in range(len(data)):
        result[data.iloc[i]["date"]] = switch[data.iloc[i]["switch"]]
    return result


if __name__ == '__main__':
    import pandas as pd

    this_code = "600030"  # 600036 # 600298 # 000858 # 000725 # 600999 # 600030
    this_data = pd.read_excel("data/code" + this_code + ".xlsx")

    this_buy_switch = pd.DataFrame([{"date": "2017-09-15", "switch": "off"}, {"date": "2019-01-11", "switch": "on"}])
    this_buy_switch.to_excel("buy_switch.xlsx")
    this_buy_switch = buy_switch_generator(this_buy_switch)

    this_functions = {"ding": {"fun": get_ding, "sliding_window": 3}, "di": {"fun": get_di, "sliding_window": 3}}
    a_trader = Trader(100000)
    a_trader, a_result, a_everyday_result = regress_trading(this_functions, this_data, a_trader, this_code,
                                                            this_buy_switch)

    a = a_trader.trading_record
    a = pd.DataFrame(a)
    print(a_result)
    print(a)
    a.to_excel(this_code + "回测结果.xlsx", index=False)
    print(a_everyday_result)
