import pandas as pd

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
                    if pd.Timestamp(trader.info["last_di"]["date"]) >  pd.Timestamp(trader.info["last_ding"]["date"]): # 连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]: # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                else:
                    if pd.Timestamp(trader.info["last_di"]["date"]) >  pd.Timestamp(trader.info["last_ding"]["date"]): # 连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]: # 上一个顶的价格比当前价格高
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
                    if pd.Timestamp(trader.info["last_di"]["date"]) >  pd.Timestamp(trader.info["last_ding"]["date"]):  # 连续底，追涨
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                    elif trader.info["last_ding"]["price"] * (1 - threshold) > stock_info["price"]:  # 上一个顶的价格比当前价格高
                        trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=0.5)
                        trader.info["first_buy"]["buy_time"] += 1
                else:
                    if pd.Timestamp(trader.info["last_di"]["date"]) >  pd.Timestamp(trader.info["last_ding"]["date"]):  # 连续底，追涨
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

# trader.last_buy = {stock_info["stock"]: {"stock": stock_info["stock"],
#                                          "quantity": 0,
#                                          "price": stock_info["price"],
#                                          }}
# elif stock_info["price"] > trader.info["last_ding"]["price"]:  # 上一个顶的价格比当前低，追涨
# trader.buy(stock_info["stock"], stock_info["price"], stock_info["date"], percentage=1)
# trader.info["first_buy"]["buy_time"] += 1