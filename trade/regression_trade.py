from ding_di import *
from trade.Trader import Trader

stock_code = "600030"


def run_functions(functions, data):
    result = []
    for fun_name in functions:
        fun = functions[fun_name]
        if fun(data):
            result.append(fun_name)

    return result


def naive_trading_strategy(info, trader, stock_info):
    if "ding" in info:
        # return "sale"
        trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    if "di" in info:
        # return "buy"
        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    return trader


def earn_percent_trading_strategy(info, trader, stock_info, threshold):
    # threshold = 0.05

    if "ding" in info:
        # return "sale"
        if stock_info["stock"] not in trader.last_buy:
            return trader

        last_price = trader.last_buy[stock_info["stock"]]["price"]
        if last_price * (1 + threshold) < stock_info["price"]:
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    if "di" in info:
        # return "buy"
        if stock_info["stock"] not in trader.last_sell:
            trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
            return trader

        last_price = trader.last_sell[stock_info["stock"]]["price"]
        if last_price * (1 - threshold) > stock_info["price"]:
            trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    return trader


def regress_trading(function_dict, data, trader):
    one_sliding = 3
    for i in range(one_sliding, len(data)):
        inter_data = data.loc[i - one_sliding: i]
        inter_data = [inter_data.iloc[j] for j in range(one_sliding)]
        ding_di = run_functions(function_dict, inter_data)
        global stock_code
        stock_info = {
            "stock": stock_code,
            "price": inter_data[-1]["close"],
            "date": inter_data[-1]["date"]
        }

        # trader = naive_trading_strategy(ding_di, trader, stock_info)
        trader = earn_percent_trading_strategy(ding_di, trader, stock_info, 0.05)

    stock_info = {
        stock_code: data.loc[len(data) - 1]["close"]
    }
    print(trader.gain_result(stock_info))

    return trader


if __name__ == '__main__':
    import pandas as pd
    this_code = "600030"  # 600036 # 600298 # 000858
    stock_code = this_code
    this_data = pd.read_excel("code" + this_code + ".xlsx")

    this_functions = {"ding": get_ding, "di": get_di}
    a_trader = Trader(100000)
    a_trader = regress_trading(this_functions, this_data, a_trader)

    a = a_trader.trading_record
    a = pd.DataFrame(a)
    a.to_excel("回测结果.xlsx", index = False)
