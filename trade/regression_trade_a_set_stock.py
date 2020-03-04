import pandas as pd
from ding_di import *
from trade.Trader import Trader
from trade.regression_trade import regress_trading
from gain_data import to_download_data_path


def run_a_stock(code):
    # code = "000725"  # 600036 # 600298 # 000858 # 000725 # 600999 # 600030

    try:
        data = pd.read_excel("data/code" + code + ".xlsx")
    except FileNotFoundError:
        to_download_data_path(code, "data/")
        data = pd.read_excel("data/code" + code + ".xlsx")

    functions = {"ding": {"fun": get_ding, "sliding_window": 3}, "di": {"fun": get_di, "sliding_window": 3}}
    # functions = {"ding": {"fun": get_ding_four, "sliding_window": 4},
    #                   "di": {"fun": get_di_four, "sliding_window": 4}}
    # functions = {"ding": {"fun": get_ding_five, "sliding_window": 5},
    #              "di": {"fun": get_di_five, "sliding_window": 5}}
    a_trader = Trader(100000)
    a_trader, a_result, a_everyday_result = regress_trading(functions, data, a_trader, code)
    a_result["stock"] = code

    a_trading_record = a_trader.trading_record

    return a_trading_record, a_result, a_everyday_result


def run_many_stock(codes):
    all_trading_record = []
    all_result = []
    all_everyday_result = []
    for i in codes:
        print("running" + i)
        try:
            a_trading_record, a_result, a_everyday_result = run_a_stock(i)
            all_trading_record.extend(a_trading_record)
            all_result.append(a_result)
            all_everyday_result.extend(a_everyday_result)
        except Exception as ex:
            print(ex)
            print(i + " fail to run")
            continue

    all_trading_record = pd.DataFrame(all_trading_record)
    all_result = pd.DataFrame(all_result)
    all_everyday_result = pd.DataFrame(all_everyday_result)
    return all_trading_record, all_result, all_everyday_result


if __name__ == '__main__':
    from trade.hu_shen_300 import hushen_300
    from trade.yanshi_50 import yangshi_50

    # stock = hushen_300[:2]
    stock = yangshi_50
    this_codes = stock["code"]  # .loc[:2]  # ["600036", "600298", "000858", "000725", "600999", "600030"]

    this_all_trading_record, this_all_result, this_all_everyday_result = run_many_stock(this_codes)

    this_all_trading_record = pd.merge(this_all_trading_record, stock[["code", "name"]], left_on="stock",
                                       right_on="code")

    this_all_result = pd.merge(this_all_result, stock[["code", "name"]], left_on="stock",
                               right_on="code")

    this_all_everyday_result = pd.merge(this_all_everyday_result, stock[["code", "name"]], left_on="stock",
                                        right_on="code")
    this_all_everyday_result_summary = this_all_everyday_result[
        ["date", "earn_percentage", "earn", "stock_value", "cash", "all"]].groupby("date").mean()
    this_all_result = this_all_result.sort_values("earn_percentage", ascending=False)
    this_all_trading_record.to_excel("trade_records.xlsx")
    this_all_result.to_excel("trade_result.xlsx")
    this_all_everyday_result_summary.to_excel("trade_every_result.xlsx")
    this_all_everyday_result.to_excel("trade_all_every_result.xlsx")
