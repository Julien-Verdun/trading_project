import yfinance as yf
from configuration import *
import matplotlib.pyplot as plt


class Action:
    """
    This class allows to get data from the stock market
    with an API
    """

    def __init__(self, name, quantity=0, period="10d"):
        self.__name = name
        self.__owed = False
        self.__quantity = quantity
        self.__cost_price = 0
        self.__action = yf.Ticker(name)
        self.__history = self.__action.history(period=period)
        return

    def getAction(self):
        return self.__action

    def getInfo(self):
        return self.__action.info

    def getCurrentValue(self):
        """
        Returns the value of the last 'close' value
        """
        return self.__history['Close'][-1]

    def getOwed(self):
        return self.__owed

    def setOwed(self, owed):
        self.__owed = owed

    def getQuantity(self):
        return self.__quantity

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getCostPrice(self):
        return self.__cost_price

    def setCostPrice(self, cost_price):
        self.__cost_price = cost_price

    def getName(self):
        return self.__name

    def getHistory(self):
        """
        Returns the history data
        """
        return self.__history

    def getCloseData(self):
        """
        Returns the 'close' column of the history data
        """
        return self.__history['Close']

    def getSupport():
        return

    def getResistance():
        return

    def getGain():
        return self.getQuantity()*(self.getCloseData()-self.getCostPrice())

    def buy(self, quantity, price):
        """
        Whenever the action is bought, the price and the quantity is updated with the 
        new quantiy and price
        """
        if not self.getOwed():
            self.setOwed(True)
            self.setQuantity(quantity)
            self.setCostPrice(price)
        else:
            self.setCostPrice((self.getQuantity()*self.getCostPrice() +
                               quantity * price)/(quantity+self.getQuantity()))
            self.setQuantity(quantity+self.getQuantity())
        return

    def sell(self, quantity):
        """
        Whenever the action is sold, the quantity is updated with the 
        new quantiy
        """
        if quantity > self.getQuantity():
            return None
        # sell all the stocks
        elif quantity == self.getQuantity():
            self.setOwed(False)
            self.setQuantity(0)
            self.setCostPrice(0)
        # stell part of the stocks
        else:
            self.setQuantity(self.getQuantity()-quantity)
        return

    def plot(self):
        plt.figure()
        print(self.getHistory().index)
        plt.plot(self.getHistory().index, self.getCloseData(), '--*')
        plt.plot(self.getHistory().index, [self.getCostPrice(
        ) for k in range(len(self.getHistory().index))], '-')
        plt.title(self.getName() + " : Stock evolution")
        plt.xlabel("Date")
        plt.ylabel("Price ($) ")
        plt.show()


name = target_companies[0]

action = Action(name, period="1m")

print(action.getCloseData())

action.buy(2, 23.4)
print(action.getCostPrice())
print(action.getQuantity())
action.buy(4, 450)
print(action.getCostPrice())
print(action.getQuantity())

action.plot()


# msft = yf.Ticker(target_companies[0])

# get stock info
# retourne un dictionnaire d'information sur la société
# print("Info : \n", msft.info)

# for key in msft.info.keys():
#     print(key, " : ", msft.info[key])


# get historical market data
# print("History : \n", msft.history(period="10d"))

# history = msft.history(period="10d")


# close_history = history['Close']

# print(close_history[:3])

# print(history.values)


# show options expirations
# print("options : \n", msft.options)


# tickers = yf.Tickers('msft aapl goog')
# # ^ returns a named tuple of Ticker objects

# # access each ticker using (example)
# tickers.msft.info
# tickers.aapl.history(period="1mo")
# tickers.goog.actions

"""
# Telechargement des données 

data = yf.download(  # or pdr.get_data_yahoo(...
    # tickers list or string as well
    tickers="MSFT",

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period="10d",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval="1d",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by='ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust=True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost=True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads=True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy=None
)
"""
