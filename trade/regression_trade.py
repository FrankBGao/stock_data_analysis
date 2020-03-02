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


def regress_trading(function_dict, data, trader, stock_code):
    data.index = range(len(data))
    max_one_slide = max([function_dict[i]["sliding_window"] for i in function_dict])
    for i in range(max_one_slide, len(data)):

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

        # trader = naive_trading_strategy(ding_di, trader, stock_info)
        # trader = earn_percent_trading_strategy(ding_di, trader, stock_info, 0.05)
        # trader = earn_percent_w_smart_start(ding_di, trader, stock_info, 0.05)
        trader = earn_percent_w_smart_start_w_small_steps(ding_di, trader, stock_info, 0.05)
        # trader = earn_percent_trading_strategy_with_safety(ding_di, trader, stock_info, 0.05, 0.1)
        # trader = earn_percent_w_safety_w_smart_start(ding_di, trader, stock_info, 0.05, 0.2)

    stock_info = {
        stock_code: data.loc[len(data) - 1]["close"]
    }
    # print(trader.gain_result(stock_info))

    return trader, trader.gain_result(stock_info)


if __name__ == '__main__':
    import pandas as pd

    this_code = "600030"  # 600036 # 600298 # 000858 # 000725 # 600999 # 600030
    this_data = pd.read_excel("data/code" + this_code + ".xlsx")

    this_functions = {"ding": {"fun": get_ding, "sliding_window": 3}, "di": {"fun": get_di, "sliding_window": 3}}
    a_trader = Trader(100000)
    a_trader, a_result = regress_trading(this_functions, this_data, a_trader, this_code)

    a = a_trader.trading_record
    a = pd.DataFrame(a)
    a.to_excel(this_code + "回测结果.xlsx", index=False)
