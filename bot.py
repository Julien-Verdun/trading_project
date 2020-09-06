from stock import Stock
from strategy import Strategy
from strategy_naive import StrategyNaive
from wallet import Wallet
# from configuration import *


class Bot:

    def __init__(self, stocks_id, date):
        # self.quantity = 1
        self.stocks_id = stocks_id
        self.stocks = [Stock(stock_id, quantity=0, date=date)
                       for stock_id in self.stocks_id]
        self.wallet = Wallet(self.stocks)
        # self.wallet.update(date)
        self.initial_account = self.wallet.virtual_account
        self.last_account = self.initial_account

    def stock_state(self, date):
        for stock in self.stocks:

            print(stock.show(date))
        print("Available cash", self.wallet.available_cash)
        print("Stocks amount", self.wallet.stocks_amount)
        return

    def run(self, date, selected_strategy):
        """
        Run strategy and update wallet 
        """

        if self.stocks[0].getDateValue(date):
            # print(selected_strategy)
            if selected_strategy == "naive":
                strategy = StrategyNaive(
                    self.stocks, date, self.wallet.available_cash)
            else:
                strategy = Strategy(self.stocks, date)
            strats = strategy.run()

            self.wallet.save_last_account()

            # for i, strat in enumerate(strats):
            #     # if the strategie says "buy" and the amount is available
            #     if strat == "buy" and self.wallet.buying_autorisation(i, 1, date):
            #         self.stocks[i].buy(
            #             self.quantity, self.stocks[i].getDateValue(date))
            #         self.wallet.buy(i, date)
            #         print("Buy " + self.stocks[i].getName())
            #     # if the strategie says "sell"
            #     elif strat == "sell" and self.stocks[i].getQuantity() > 0:
            #         self.stocks[i].sell()
            #         self.wallet.sell(i, date)
            #         print("Sell " + self.stocks[i].getName())
            #     else:
            #         print("No go")

            for i, strat in enumerate(strats):
                # if the strategie says "buy" and the amount is available
                if strat[0] == "buy" and strat[1] > 0 and self.wallet.buying_autorisation(i, strat[1], date):
                    self.stocks[i].buy(
                        strat[1], self.stocks[i].getDateValue(date))
                    self.wallet.buy(i, date, strat[1])
                    print(
                        "Buy " + str(strat[1]) + " stock(s) of " + self.stocks[i].getName())
                # if the strategie says "sell"
                elif strat[0] == "sell" and self.stocks[i].getQuantity() > 0:
                    self.stocks[i].sell()
                    self.wallet.sell(i, date)
                    print(
                        "Sell " + str(self.stocks[i].getQuantity()) + " stock(s) of " + self.stocks[i].getName())
                else:
                    print("No go")

            self.wallet.update(date)

            self.last_account = self.wallet.virtual_account
            print("Date : ", date, "Wallet account : ", self.wallet.virtual_account, ", Stocks amount : ", self.wallet.stocks_amount, ", Available cash : ", self.wallet.available_cash, "\nVariation with previous day : ",
                  int(10000*(self.wallet.virtual_account-self.wallet.last_account)/self.wallet.virtual_account)/100)
