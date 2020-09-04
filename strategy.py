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
            historical_data = stock.getCloseData()
            pos_var, neg_var = [], []

            # Calculation of the RSI
            # for v in historical_data["Variation"].tolist():
            for i in range(len(historical_data["Variation"].tolist())):
                if historical_data.index[i].timestamp() <= time.mktime(time.strptime(self.__date, "%Y-%m-%d")):
                    if historical_data["Variation"].tolist()[i] > 0:
                        pos_var.append(
                            historical_data["Variation"].tolist()[i])
                        neg_var.append(0)
                    else:
                        neg_var.append(
                            historical_data["Variation"].tolist()[i])
                        pos_var.append(0)
                else:
                    break
            avg_gain, avg_loss = abs(np.mean(pos_var)), abs(np.mean(neg_var))
            # rsi_step_one = 100 * (1 - (1/(1 + (avg_gain/avg_loss))))
            rsi_step_one = 100 * avg_gain / (avg_gain + avg_loss)
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
                    result.append(["no go", np.nan])
        return result
