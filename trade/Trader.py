class Trader:
    def __init__(self, invest):
        self.invest = invest
        self.all_money = invest
        self.holding_stock = {}
        self.trading_record = []
        self.last_buy = {}
        self.last_sell = {}
        self.info = {}

    def buy(self, stock, price, date, quantity=None, percentage=None, option=None):
        could_buy = self.all_money // (price * 100)
        # print("buy:" + option + "_" + str(percentage))

        if could_buy <= 1:
            return

        if quantity is None:
            if percentage is None:
                quantity = could_buy
            else:
                quantity = int(could_buy * percentage)
        elif not percentage is None:
            if could_buy < quantity:
                quantity = could_buy

        if quantity <= 1:
            return

        amount = quantity * price * 100

        self.all_money = self.all_money - amount

        if stock not in self.holding_stock:
            self.holding_stock[stock] = {
                "stock": stock,
                "quantity": quantity,
            }
        else:
            self.holding_stock[stock]["quantity"] += quantity

        self.last_buy = {stock: {"stock": stock,
                                 "quantity": quantity,
                                 "price": price,
                                 }}
        inter = {
            "stock": stock,
            "price": price,
            "quantity": quantity,
            "amount": amount,
            "type_is": "buy",
            "date": date,
            "option": option
        }
        self.trading_record.append(inter)
        # print(inter)

    def sell(self, stock, price, date, quantity=None, percentage=None, option=None):
        if stock in self.holding_stock:
            could_sell = self.holding_stock[stock]["quantity"]
        else:
            return
        # print("sell:" + option + "_" + str(percentage))
        if quantity is None:
            if percentage is None:
                quantity = could_sell
            else:
                quantity = int(could_sell * percentage)
        elif not percentage is None:
            if could_sell < quantity:
                quantity = could_sell

        amount = quantity * price * 100
        self.all_money = self.all_money + amount

        if could_sell == quantity:
            self.holding_stock.pop(stock)
            holding_stock_value = 0
        else:
            self.holding_stock[stock]["quantity"] -= quantity
            holding_stock_value = self.holding_stock[stock]["quantity"] * price * 100

        self.last_sell = {stock: {"stock": stock,
                                  "quantity": quantity,
                                  "price": price,
                                  }
                          }

        inter = {
            "stock": stock,
            "price": price,
            "quantity": quantity,
            "amount": amount,
            "type_is": "sell",
            "all_money": self.all_money,
            "date": date,
            "earn_percentage": (self.all_money + holding_stock_value - self.invest) / self.invest,
            "option":option
        }
        self.trading_record.append(inter)
        # print(inter)

    def gain_all_trade_record(self):
        return self.trading_record

    def gain_holding(self):
        return self.holding_stock

    def gain_result(self, current_stock_prices):
        holding_value = 0
        for i in self.holding_stock:
            inter = self.holding_stock[i]
            holding_quantity = inter["quantity"]
            this_stock_price = current_stock_prices[i]
            holding_value += holding_quantity * this_stock_price * 100

        return {
            "cash": self.all_money,
            "stock_value": holding_value,
            "all": self.all_money + holding_value,
            "earn": self.all_money + holding_value - self.invest,
            "earn_percentage": (self.all_money + holding_value - self.invest) / self.invest
        }
