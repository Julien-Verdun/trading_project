import numpy as np
import time
from configuration import *


class StrategyNaive:
    """
    This class will define the buy and sell strategy
    """

    def __init__(self, stocks, date):
        self.__stocks = stocks
        self.__date = date

    def run(self):
        result = []
        for stock in self.__stocks:
            historical_data = stock.getCloseData()

            # variation moyenne
            mean_var = 0
            for i in range(len(historical_data["Variation"].tolist())):
                if historical_data.index[i].timestamp() <= time.mktime(time.strptime(self.__date, "%Y-%m-%d")):
                    mean_var += 100*historical_data["Variation"].tolist()[i]
                else:
                    break
            mean_var = np.mean(mean_var)
            print("Mean variation : ", mean_var)

            if lower < mean_var < upper:
                result.append("no go")
            elif mean_var >= upper:
                result.append("buy")
            elif mean_var < lower:
                result.append("sell")

        return result
