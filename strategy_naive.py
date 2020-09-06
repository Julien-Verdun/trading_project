import numpy as np
import time
from configuration import *


class StrategyNaive:
    """
    This class will define the buy and sell strategy :
    the strategy is pretty simple, every day, it computes the mean variation of the stock price between
    the current day and the first day of the simulation and decides whether or not the bot should buy
    the stock. If the mean variation is higher than a defined threshold, the bot buys the stock, 
    if it is lower than a defined threshold, the bot sells the stock, otherwise, it does nothing.
    """

    def __init__(self, stocks, date, available_cash):
        self.__stocks = stocks
        self.__date = date
        self.__available_cash = available_cash

    def run(self):
        result = []
        for stock in self.__stocks:

            # mean variation
            # historical_data = stock.getCloseData()
            # mean_var = 0
            # for i in range(len(historical_data["Variation"].tolist())):
            #     if historical_data.index[i].timestamp() <= time.mktime(time.strptime(self.__date, "%Y-%m-%d")):
            #         if (time.mktime(time.strptime(self.__date, "%Y-%m-%d"))-historical_data.index[i].timestamp()) / (24 * 3600) <= moving_window:
            #             mean_var += 100 * \
            #                 historical_data["Variation"].tolist()[i]
            #     else:
            #         break
            # mean_var = np.mean(mean_var)

            mean_var = stock.getMeanVariation(self.__date)

            if lower < mean_var < upper:
                result.append("no go")
            elif mean_var >= upper:
                result.append("buy")
            elif mean_var < lower:
                result.append("sell")

        return self.optimize_quantity(result)

    def optimize_quantity(self, result):
        """
        Takes the list of actions no go - buy - sell and returns for each stock
        the action and the stock's quantity to buy if action is buy 
        """
        # calculation of the available cash after selling the actions
        available_cash = self.__available_cash
        stock_to_buy = []
        for i in range(len(self.__stocks)):
            stock_to_buy.append(i)
            if result[i] == "sell":
                available_cash += self.__stocks[i].getQuantity() * \
                    self.__stocks[i].getDateValue(self.__date)

        # sorting stock's to buy by ascending value of variation
        stock_to_buy_sorted = [0]*len(stock_to_buy)
        variation_list = [self.__stocks[i].getMeanVariation(
            self.__date) for i in stock_to_buy]

        for i in range(len(stock_to_buy)):
            stock_to_buy_sorted[i] = stock_to_buy[np.argsort(variation_list)[
                ::-1][i]]

        # calculation of the quantity of stock to buy, by trying to maximise the gain
        # the bot should by the stock that will provide the more money (the maximum variation from a day to another)
        result_with_quantity = [[result[i], 0] for i in range(len(result))]
        for elt in stock_to_buy_sorted:
            result_with_quantity[elt][1] = available_cash//self.__stocks[elt].getDateValue(
                self.__date)
            available_cash -= self.__stocks[elt].getDateValue(self.__date) * (
                available_cash//self.__stocks[elt].getDateValue(self.__date))

        return result_with_quantity
