from stock import Stock
from strategy import Strategy
from strategy_naive import StrategyNaive
from wallet import Wallet


class Bot:

    def __init__(self, stocks_id, date):
        self.quantity = 1
        self.stocks_id = stocks_id
        self.stocks = [Stock(stock_id, quantity=1, date=date)
                       for stock_id in self.stocks_id]
        self.wallet = Wallet(self.stocks)
        self.wallet.update(date)
        self.initial_account = self.wallet.account
        self.last_account = self.initial_account

    def run(self, date):
        """
        Run strategy and update wallet 
        """

        if self.stocks[0].getDateValue(date):
            # strategy = Strategy(self.stocks, date)
            strategy = StrategyNaive(self.stocks, date)
            strats = strategy.run()

            for i, strat in enumerate(strats):
                if strat == "buy":
                    self.stocks[i].buy(
                        self.quantity, self.stocks[i].getDateValue(date))

                elif strat == "sell":
                    self.stocks[i].sell(self.quantity)

            self.wallet.update(date)
            self.last_account = self.wallet.account
            print("Date : ", date, "Wallet account : ", self.wallet.account, "Variation with previous day : ",
                  int(10000*(self.wallet.account-self.wallet.last_account)/self.wallet.account)/100)
        else:
            print(date, " is not a trading day ! ")
