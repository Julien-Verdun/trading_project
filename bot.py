from stock import Stock
from strategy import Strategy
from strategy_naive import StrategyNaive
from wallet import Wallet
from configuration import *


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

    def stock_state(self):
        for stock in self.stocks:
            print(stock.show())
        return

    def run(self, date):
        """
        Run strategy and update wallet 
        """

        if self.stocks[0].getDateValue(date):
            if selected_strategy == "naive":
                strategy = StrategyNaive(self.stocks, date)
            else:
                strategy = Strategy(self.stocks, date)
            strats = strategy.run()

            self.wallet.save_last_account()

            for i, strat in enumerate(strats):
                if strat == "buy":
                    self.stocks[i].buy(
                        self.quantity, self.stocks[i].getDateValue(date))
                    print("Buy " + self.stocks[i].getName())
                elif strat == "sell" and self.stocks[i].getQuantity() > 0:
                    self.stocks[i].sell()
                    self.wallet.sell(i, date)
                    print("Sell " + self.stocks[i].getName())
                else:
                    print("No go")
            self.wallet.update(date)

            # self.wallet.update(date)
            self.last_account = self.wallet.virtual_account
            print("Date : ", date, "Wallet account : ", self.wallet.virtual_account, "\nVariation with previous day : ",
                  int(10000*(self.wallet.virtual_account-self.wallet.last_account)/self.wallet.virtual_account)/100)
        # else:
        #     print(date, " is not a trading day ! ")
