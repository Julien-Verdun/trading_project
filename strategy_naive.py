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

    def __init__(self, stocks, date):
        self.__stocks = stocks
        self.__date = date

    def run(self):
        result = []
        for stock in self.__stocks:
            historical_data = stock.getCloseData()

            # mean variation
            mean_var = 0
            moving_window = 30
            for i in range(len(historical_data["Variation"].tolist())):
                if historical_data.index[i].timestamp() <= time.mktime(time.strptime(self.__date, "%Y-%m-%d")):
                    if (time.mktime(time.strptime(self.__date, "%Y-%m-%d"))-historical_data.index[i].timestamp()) / (24 * 3600) <= moving_window:
                        mean_var += 100 * \
                            historical_data["Variation"].tolist()[i]
                else:
                    break
            mean_var = np.mean(mean_var)

            if lower < mean_var < upper:
                result.append("no go")
            elif mean_var >= upper:
                result.append("buy")
            elif mean_var < lower:
                result.append("sell")

        return result
