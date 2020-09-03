import pandas as pd


class Strategy:
    """
    This class will define the buy and sell strategy
    """
    def __init__(self, stocks):
        self.__stocks = stocks
        return
    def run(self):
        for stock in self.__stocks:
            historical_data = stock.getCloseData()

            rsi_step_one = 100 * (1 - (1/(1 + (avg_gain/avg_loss))))

print("test")
