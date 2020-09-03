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
            historical_data = stock.getCloseData().tolist()
            """
            pos_values, neg_values = [], []
            for p in historical_data:
                if p > 0:
                    p.append
            """

            #rsi_step_one = 100 * (1 - (1/(1 + (avg_gain/avg_loss))))
            print("OK")
