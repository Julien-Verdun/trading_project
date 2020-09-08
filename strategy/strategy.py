import numpy as np
import time


class Strategy:
    """
    This class will define the buy and sell strategy
    """

    def __init__(self, stocks, date, unit_price, sell_threshold, buy_threshold):
        self.__stocks = stocks
        self.__date = date
        self.__unit_price = unit_price
        self.__sell_threshold = sell_threshold
        self.__buy_threshold = buy_threshold

    def run(self):
        result = []
        for stock in self.__stocks:
            # Calculation of the RSI
            rsi_step_one = stock.getRSI(self.__date)

            stock_price = stock.getDateValue(self.__date)

            if self.__buy_threshold < rsi_step_one < self.__sell_threshold:
                result.append(["no go", np.nan])
            elif rsi_step_one < self.__buy_threshold:
                factor = (self.__buy_threshold - rsi_step_one) / 10
                amount = factor * self.__unit_price
                nb_stocks = amount // stock_price
                if amount >= stock_price:
                    result.append(["buy", nb_stocks])
                else:
                    result.append(["no go", np.nan])
            else:
                factor = (rsi_step_one - self.__sell_threshold) / 10
                amount = factor * self.__unit_price
                nb_stocks = amount // stock_price
                if amount >= stock_price:
                    result.append(["sell", nb_stocks])
                else:
                    result.append(["no go", nb_stocks])
        return result
