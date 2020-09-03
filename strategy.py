import numpy as np

class Strategy:
    """
    This class will define the buy and sell strategy
    """
    def __init__(self, stocks):
        self.__stocks = stocks
        

    def run(self):
        result = []
        for stock in self.__stocks:
            historical_data = stock.getCloseData()
            pos_var, neg_var = [], []

            # Calculation of the RSI
            for v in historical_data["Variation"].tolist():
                if v > 0:
                    pos_var.append(v)
                    neg_var.append(0)
                else:
                    neg_var.append(v)
                    pos_var.append(0)
            avg_gain, avg_loss = abs(np.mean(pos_var)), abs(np.mean(neg_var))
            rsi_step_one = 100 * (1 - (1/(1 + (avg_gain/avg_loss))))

            # Calculation of a smooth RSI
            n = historical_data.shape[0] - 1
            current = historical_data["Variation"].tolist()[-1]
            if current > 0:
                current_gain = current
                current_loss = 0
            else:
                current_gain = 0
                current_loss = current

            rsi_step_two = 100 * (1 - (1/(1 + ((avg_gain * n + current_gain)/(avg_loss * n + current_loss)))))

            if 30 < rsi_step_one < 70:
                result.append("no go")
            elif rsi_step_one <= 30:
                result.append("buy")
            else:
                result.append("sell")
                
        return result
