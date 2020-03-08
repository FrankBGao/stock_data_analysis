import pandas as pd


# this is the benchmark
def dummy_strategy(info, trader, stock_info):
    if "buy" not in trader.info:
        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
        trader.info["buy"] = []
        return trader
    return trader


# this is the naive benchmark
def naive_trading_strategy(info, trader, stock_info, buy_switch=True):
    if "ding" in info:
        # return "sale"
        trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader

    if not buy_switch:
        return trader

    if "di" in info:
        # return "buy"
        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    return trader


# this is the naive benchmark
def naive_w_cold_down(info, trader, stock_info, cold_down_period="30 day"):
    if "cold_down_deadline" not in trader.info:
        # trader 数据初始化
        trader.info["cold_down_deadline"] = ""

    # safety check cold down
    if trader.info["cold_down_deadline"] != "":
        if pd.Timestamp(stock_info["date"]) < trader.info["cold_down_deadline"]:
            return trader
        else:
            trader.info["cold_down_deadline"] = ""

    if "ding" in info:
        # return "sale"
        trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])

        if stock_info["stock"] in trader.last_buy:
            if trader.last_buy[stock_info["stock"]]["price"] > trader.last_sell[stock_info["stock"]]["price"]:
                trader.info["cold_down_deadline"] = pd.Timestamp(stock_info["date"]) + pd.Timedelta(cold_down_period)
        return trader
    if "di" in info:
        # return "buy"
        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    return trader


# this is the naive threshold
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


# this is the naive threshold and safety
def earn_percent_trading_strategy_with_safety(info, trader, stock_info, threshold, safety=0.1):
    # threshold = 0.05

    # safety
    if stock_info["stock"] in trader.last_buy and stock_info["stock"] in trader.holding_stock:
        holding_price = trader.last_buy[stock_info["stock"]]["price"]
        if holding_price > stock_info["price"] * (1 + safety):
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
            return trader

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


def earn_percent_w_smart_start(info, trader, stock_info, threshold):
    # threshold = 0.05
    if "ding_di" not in trader.info:
        trader.info["ding_di"] = []

    if "ding" in info:
        # return "sale"
        if "ding" not in trader.info["ding_di"]:
            trader.info["ding_di"].append("ding")
            return trader

        if stock_info["stock"] not in trader.last_buy:
            return trader

        last_price = trader.last_buy[stock_info["stock"]]["price"]
        if last_price * (1 + threshold) < stock_info["price"]:
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader

    if "di" in info:
        # return "buy"
        if "di" not in trader.info["ding_di"]:
            trader.info["ding_di"].append("di")
            return trader

        if stock_info["stock"] not in trader.last_sell:
            trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
            return trader

        last_price = trader.last_sell[stock_info["stock"]]["price"]
        if last_price * (1 - threshold) > stock_info["price"]:
            trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    return trader


def earn_percent_w_smart_start_w_small_steps(info, trader, stock_info, threshold):
    # threshold = 0.05

    if "ding_di" not in trader.info:
        # trader 数据初始化
        trader.info["ding_di"] = []
        trader.info["first_buy"] = {
            "price": 0,
            "buy_time": 0
        }
        trader.info["last_ding"] = {
            "price": 0,
            "date": 0
        }
        trader.info["last_di"] = {
            "price": 0,
            "date": 0
        }

    if "ding" in info:
        # return "sale"
        trader.info["last_ding"] = {
            "price": stock_info["price"],
            "date": stock_info["date"]
        }
        if "ding" not in trader.info["ding_di"]:
            # smart first sell
            trader.info["ding_di"].append("ding")
            return trader

        if stock_info["stock"] not in trader.last_buy:
            return trader
        # 一段式卖出
        last_price = trader.info["first_buy"]["price"]
        if last_price * (1 + threshold) < stock_info["price"]:
            trader.info["first_buy"]["price"] = 0
            trader.info["first_buy"]["buy_time"] = 0
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader

    if "di" in info:
        # return "buy"

        if "di" not in trader.info["ding_di"]:
            # smart first buy
            trader.info["ding_di"].append("di")
            trader.info["last_di"] = {
                "price": stock_info["price"],
                "date": stock_info["date"]
            }
            return trader

        if stock_info["stock"] not in trader.last_sell:
            # 三段式购买
            if trader.info["first_buy"]["price"] == 0:
                trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                trader.info["first_buy"]["price"] = stock_info["price"]
                trader.info["first_buy"]["buy_time"] = 1
            else:
                if trader.info["first_buy"]["buy_time"] == 1:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                else:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 再一个连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
            return trader

        last_price = trader.last_sell[stock_info["stock"]]["price"]
        if last_price * (1 - threshold) > stock_info["price"]:
            # 三段式购买
            if trader.info["first_buy"]["price"] == 0:
                trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                trader.info["first_buy"]["price"] = stock_info["price"]
                trader.info["first_buy"]["buy_time"] = 1
            else:
                if trader.info["first_buy"]["buy_time"] == 1:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                else:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 再一个连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
        trader.info["last_di"] = {
            "price": stock_info["price"],
            "date": stock_info["date"]
        }
        return trader
    return trader


def earn_percent_w_safety_w_smart_start(info, trader, stock_info, threshold, safety=0.1):
    # threshold = 0.05
    if "ding_di" not in trader.info:
        trader.info["ding_di"] = []

    # safety
    if stock_info["stock"] in trader.last_buy and stock_info["stock"] in trader.holding_stock:
        holding_price = trader.last_buy[stock_info["stock"]]["price"]
        if holding_price > stock_info["price"] * (1 + safety):
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
            return trader

    if "ding" in info:
        # return "sale"
        if "ding" not in trader.info["ding_di"]:
            trader.info["ding_di"].append("ding")
            return trader

        if stock_info["stock"] not in trader.last_buy:
            return trader

        last_price = trader.last_buy[stock_info["stock"]]["price"]
        if last_price * (1 + threshold) < stock_info["price"]:
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader

    if "di" in info:
        # return "buy"
        if "di" not in trader.info["ding_di"]:
            trader.info["ding_di"].append("di")
            return trader

        if stock_info["stock"] not in trader.last_sell:
            trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
            return trader

        last_price = trader.last_sell[stock_info["stock"]]["price"]
        if last_price * (1 - threshold) > stock_info["price"]:
            trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader
    return trader


def earn_percent_w_smart_start_w_small_steps_w_safety(info, trader, stock_info, threshold, safety,
                                                      cold_down_period="30 day"):
    # threshold = 0.05

    if "safety_sell" not in trader.info:
        # trader 数据初始化
        trader.info["ding_di"] = []
        trader.info["first_buy"] = {
            "price": 0,
            "buy_time": 0
        }
        trader.info["safety_sell"] = {
            "price": 0,
            "date": "",
            "cold_down_deadline": ""
        }
        trader.info["last_ding"] = {
            "price": 0,
            "date": 0
        }
        trader.info["last_di"] = {
            "price": 0,
            "date": 0
        }
    # safety check cold down
    if trader.info["safety_sell"]["cold_down_deadline"] != "":
        if pd.Timestamp(stock_info["date"]) < trader.info["safety_sell"]["cold_down_deadline"]:
            return trader
        else:
            trader.info["safety_sell"]["date"] = ""
            trader.info["safety_sell"]["cold_down_deadline"] = ""

    # safety
    if stock_info["stock"] in trader.holding_stock:
        holding_price = trader.last_buy[stock_info["stock"]]["price"]
        last_safety_sell_price = trader.info["safety_sell"]["price"]
        if last_safety_sell_price != 0:
            need_price = min(last_safety_sell_price, holding_price)
        else:
            need_price = holding_price

        if need_price > stock_info["price"] * (1 + safety):
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)

            trader.info["ding_di"] = []
            trader.info["safety_sell"] = {
                "price": stock_info["price"],
                "date": stock_info["date"],
                "cold_down_deadline": pd.Timestamp(stock_info["date"]) + pd.Timedelta(cold_down_period)
            }
            return trader

    if "ding" in info:
        # return "sale"
        trader.info["last_ding"] = {
            "price": stock_info["price"],
            "date": stock_info["date"]
        }
        if "ding" not in trader.info["ding_di"]:
            # smart first sell
            trader.info["ding_di"].append("ding")
            return trader

        if stock_info["stock"] not in trader.last_buy:
            return trader
        # 一段式卖出
        last_price = trader.info["first_buy"]["price"]
        if last_price * (1 + threshold) < stock_info["price"]:
            trader.info["first_buy"]["price"] = 0
            trader.info["first_buy"]["buy_time"] = 0
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"])
        return trader

    if "di" in info:
        # return "buy"

        if "di" not in trader.info["ding_di"]:
            # smart first buy
            trader.info["ding_di"].append("di")
            trader.info["last_di"] = {
                "price": stock_info["price"],
                "date": stock_info["date"]
            }
            return trader

        if stock_info["stock"] not in trader.last_sell:
            # 三段式购买
            if trader.info["first_buy"]["price"] == 0:
                trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                trader.info["first_buy"]["price"] = stock_info["price"]
                trader.info["first_buy"]["buy_time"] = 1
            else:
                if trader.info["first_buy"]["buy_time"] == 1:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                else:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 再一个连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
            return trader

        last_price = trader.last_sell[stock_info["stock"]]["price"]
        if last_price * (1 - threshold) > stock_info["price"]:
            # 三段式购买
            if trader.info["first_buy"]["price"] == 0:
                trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                trader.info["first_buy"]["price"] = stock_info["price"]
                trader.info["first_buy"]["buy_time"] = 1
            else:
                if trader.info["first_buy"]["buy_time"] == 1:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                else:
                    if pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(
                            trader.info["last_ding"]["date"]):  # 再一个连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
        trader.info["last_di"] = {
            "price": stock_info["price"],
            "date": stock_info["date"]
        }
        return trader
    return trader


def three_step_buy_select(steps, up_down):
    stra = ["sensitive", "normal", "bold"]
    index_of = stra.index(steps)
    index_of = index_of + up_down
    # print(steps, str(up_down), index_of)
    if index_of <= 0:
        return stra[0]
    if index_of >= len(stra) - 1:
        return stra[-1]
    return stra[index_of]


def earn_percent_w_smart_start_w_small_steps_w_safety_double(info, trader, stock_info,
                                                             up_threshold,
                                                             down_threshold,
                                                             safety_down,
                                                             safety_up,
                                                             buy_switch=True,
                                                             initial_step="normal",
                                                             cold_down_period="30 day"):
    # threshold = 0.05
    sensitive = 2
    three_step_buy = {
        "sensitive": [0.25, 0.25, 0],
        "normal": [0.5, 0.5, 1],
        "bold": [0.75, 1, 1]
    }
    """

    :param info:
    :param trader:
    :param stock_info:
    :param threshold: 距离上次交易的价差
    :param safety_down: 跌了，害怕，跑
    :param safety_up: 涨了，挣了，跑
    :param cold_down_period:
    :param initial_step: normal, sensitive, bold
    :return:
    """
    if "safety_sell" not in trader.info:
        # trader 数据初始化
        trader.info["ding_di"] = []
        trader.info["first_buy"] = {
            "price": 0,
            "buy_time": 0
        }
        trader.info["safety_sell"] = {
            "price": 0,
            "date": "",
            "cold_down_deadline": "",
            "cold_down_period": "",
            "safety_down": safety_down
        }
        trader.info["last_ding"] = {
            "price": 0,
            "date": 0
        }
        trader.info["last_di"] = {
            "price": 0,
            "date": 0
        }
        trader.info["profit_sell"] = {
            "price": 0,
            "date": 0
        }
        trader.info["three_step_buy"] = initial_step

    three_step_buy_strategy = trader.info["three_step_buy"]

    if trader.info["safety_sell"]["cold_down_period"] == "":
        cold_down_period = pd.Timedelta(cold_down_period)
        safety_down = safety_down
    else:
        cold_down_period = trader.info["safety_sell"]["cold_down_period"]
        safety_down = trader.info["safety_sell"]["safety_down"]

    # safety check cold down
    if trader.info["safety_sell"]["cold_down_deadline"] != "":
        if pd.Timestamp(stock_info["date"]) < trader.info["safety_sell"]["cold_down_deadline"]:
            return trader
        else:
            trader.info["safety_sell"]["date"] = ""
            trader.info["safety_sell"]["cold_down_deadline"] = ""

    # safety
    if stock_info["stock"] in trader.holding_stock:
        holding_price = trader.last_buy[stock_info["stock"]]["price"]
        last_safety_sell_price = trader.info["safety_sell"]["price"]
        if last_safety_sell_price != 0:
            need_price = min(last_safety_sell_price, holding_price)
        else:
            need_price = holding_price

        # 跌怕了，半仓，冷静一段时间
        if need_price > stock_info["price"] * (1 + safety_down):
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5,
                        option="lost_safe")

            # trader.info["ding_di"] = []
            trader.info["safety_sell"] = {
                "price": stock_info["price"],
                "date": stock_info["date"],
                "cold_down_deadline": pd.Timestamp(stock_info["date"]) + cold_down_period,
                "cold_down_period": cold_down_period * sensitive,
                "safety_down": safety_down / sensitive
            }
            # 惩罚，更小心一点
            trader.info["three_step_buy"] = three_step_buy_select(trader.info["three_step_buy"], -1)
            trader.info["first_buy"]["buy_time"] = 0
            return trader
        # 落袋为安， 半仓
        elif stock_info["price"] > (1 + safety_up) * trader.info["first_buy"]["price"]:
            if trader.info["profit_sell"]["price"] == 0 or stock_info["price"] > (1 + safety_up) * trader.info["profit_sell"]["price"]:
                trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5,
                            option="earn_safe")
                trader.info["profit_sell"] = {
                    "price": stock_info["price"],
                    "date": stock_info["date"]
                }
                trader.info["first_buy"]["buy_time"] = 0
                # 奖励更大胆一些
                trader.info["three_step_buy"] = three_step_buy_select(trader.info["three_step_buy"], 1)
                if trader.info["safety_sell"]["cold_down_period"] != "":
                    trader.info["safety_sell"]["cold_down_period"] = trader.info["safety_sell"][
                                                                         "cold_down_period"] / sensitive
                    inter_safety_down = trader.info["safety_sell"]["safety_down"] * (1 + 0.1 * sensitive)
                    if inter_safety_down > 0.3:
                        trader.info["safety_sell"]["safety_down"] = 0.3
                    else:
                        trader.info["safety_sell"]["safety_down"] = inter_safety_down

    if "ding" in info:
        # return "sale"
        trader.info["last_ding"] = {
            "price": stock_info["price"],
            "date": stock_info["date"]
        }
        if "ding" not in trader.info["ding_di"]:
            # smart first sell
            trader.info["ding_di"].append("ding")
            return trader

        if stock_info["stock"] not in trader.last_buy:
            return trader
        # 一段式卖出
        last_price = trader.info["first_buy"]["price"]
        if last_price * (1 + up_threshold) < stock_info["price"]:
            trader.info["first_buy"]["price"] = 0
            trader.info["first_buy"]["buy_time"] = 0
            trader.info["profit_sell"]["price"] = 0
            trader.info["profit_sell"]["date"] = 0
            trader.sell(stock_info["stock"], stock_info["price"], stock_info["date"], option="ding")
        return trader

    if not buy_switch:
        return trader

    if "di" in info:
        # return "buy"

        if "di" not in trader.info["ding_di"]:
            # smart first buy
            trader.info["ding_di"].append("di")
            trader.info["last_di"] = {
                "price": stock_info["price"],
                "date": stock_info["date"]
            }
            return trader

        # 第一次买
        if stock_info["stock"] not in trader.last_sell:

            # 三段式购买
            if trader.info["first_buy"]["buy_time"] == 0:
                trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"],
                           percentage=three_step_buy[three_step_buy_strategy][0],
                           option="f_1" + three_step_buy_strategy)
                trader.info["first_buy"]["price"] = stock_info["price"]
                trader.info["first_buy"]["buy_time"] = 1
            else:
                # 连续底，追涨
                cond_1 = pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(trader.info["last_ding"]["date"])
                # 上一个顶的价格比当前价格高
                cond_2 = trader.info["last_ding"]["price"] * (1 - up_threshold) > stock_info["price"]
                if trader.info["first_buy"]["buy_time"] == 1:
                    if cond_1 or cond_2:  # 追买 25%
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"],
                                   percentage=three_step_buy[three_step_buy_strategy][1],
                                   option="f_2" + three_step_buy_strategy)
                        trader.info["first_buy"]["buy_time"] += 1
                elif trader.info["first_buy"]["buy_time"] == 2:
                    if cond_1 or cond_2:  # 追买 25%
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"],
                                   percentage=three_step_buy[three_step_buy_strategy][2],
                                   option="f_3" + three_step_buy_strategy)
                        trader.info["first_buy"]["buy_time"] += 1
            return trader

        last_price = trader.last_sell[stock_info["stock"]]["price"]
        last_date = trader.last_sell[stock_info["stock"]]["date"]
        if last_price == trader.info["safety_sell"]["price"]:
            cond = True
        else:
            cond = last_price * (1 - down_threshold) > stock_info["price"] or \
                   trader.info["last_ding"]["price"] * (1 - down_threshold) > stock_info["price"] or \
                   ((5<len(pd.bdate_range(min(pd.Timestamp(trader.info["last_ding"]["date"]), pd.Timestamp(last_date)),
                                        stock_info["date"])) < 15) and
                    last_price * (1 + down_threshold) < stock_info["price"])
        if cond:
            # 三段式购买
            if trader.info["first_buy"]["buy_time"] == 0:
                trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"],
                           percentage=three_step_buy[three_step_buy_strategy][1],
                           option="a_1" + three_step_buy_strategy)
                trader.info["first_buy"]["price"] = stock_info["price"]
                trader.info["first_buy"]["buy_time"] = 1
            else:
                # 连续底，追涨
                cond_1 = pd.Timestamp(trader.info["last_di"]["date"]) > pd.Timestamp(trader.info["last_ding"]["date"])
                # 上一个顶的价格比当前价格高
                cond_2 = trader.info["last_ding"]["price"] * (1 - down_threshold) > stock_info["price"]
                if trader.info["first_buy"]["buy_time"] == 1:
                    if cond_1 or cond_2:  # 追买 25%
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"],
                                   percentage=three_step_buy[three_step_buy_strategy][1],
                                   option="a_2" + three_step_buy_strategy)
                        trader.info["first_buy"]["buy_time"] += 1
                elif trader.info["first_buy"]["buy_time"] == 2:
                    if cond_1 or cond_2:  # 追买 25%
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"],
                                   percentage=three_step_buy[three_step_buy_strategy][2],
                                   option="a_3" + three_step_buy_strategy)
                        trader.info["first_buy"]["buy_time"] += 1

        trader.info["last_di"] = {
            "price": stock_info["price"],
            "date": stock_info["date"]
        }
        return trader
    return trader

# trader.last_buy = {stock_info["stock"]: {"stock": stock_info["stock"],
#                                          "quantity": 0,
#                                          "price": stock_info["price"],
#                                          }}
# elif stock_info["price"] > trader.info["last_ding"]["price"]:  # 上一个顶的价格比当前低，追涨
# trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
# trader.info["first_buy"]["buy_time"] += 1
