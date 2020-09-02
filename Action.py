import yfinance as yf


msft = yf.Ticker("MSFT")
print(dir(msft))

print(msft.info)

print(msft.history(period="max"))


class Action:
    """
    This class allows to get data from the stock market 
    with an API
    """

    def __init__(self, name, cost_price, quantity=0):
        self.__name = name
        self.__quantity = quantity
        self.__cost_price = cost_price
        # 6 derniers jours : valeur du cours à la fin de la séance
        # resistances et supports
        return

    def getCurrentValue(self):
        """
        retrun the value of the 
        """
        return

    def buy(self):
        return

    def sell(self):
        return

    def getData(self):
        return
