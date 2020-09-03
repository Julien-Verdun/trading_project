import yfinance as yf
import time
from configuration import *
import matplotlib.pyplot as plt


class Stock:
    """
    This class allows to get data from the stock market
    with an API
    """

    def __init__(self, name, date, quantity=0):
        self.__name = name
        self.__owned = False
        self.__quantity = quantity
        self.__cost_price = 0
        self.__stock = yf.Ticker(name)
        self.__history = self.__stock.history(
            start=time.strftime("%Y-%m-%d", time.gmtime(
                time.mktime(time.strptime(date, "%Y-%m-%d")) - 30*24*3600)),
            end=time.strftime("%Y-%m-%d", time.gmtime(
                time.mktime(time.strptime(date, "%Y-%m-%d")) + simulation_time*24*3600))
        )
        return

    def getStock(self):
        """
        Returns the stock object
        """
        return self.__stock

    def getInfo(self):
        """
        Returns the stock informations
        """
        return self.__stock.info

    def getCurrentValue(self):
        """
        Returns the value of the last 'close' value
        """
        return self.__history['Close'][-1]

    def getDateValue(self, date):
        """
        Returns the value of the 'close' value for date "date" (format year - month - day)
        """
        return self.__history['Close'][date]

    def getOwned(self):
        """
        Returns a booleen, whether or not the stock is owned
        """
        return self.__owned

    def setOwned(self, owned):
        """
        Sets a booleen, whether or not the stock is owned
        """
        self.__owned = owned

    def getQuantity(self):
        """
        Returns the stock's quantity
        """
        return self.__quantity

    def setQuantity(self, quantity):
        """
        Sets the stock's quantity
        """
        self.__quantity = quantity

    def getCostPrice(self):
        """
        Returns the stock cost price
        """
        return self.__cost_price

    def setCostPrice(self, cost_price):
        """
        Sets the stock cost price
        """
        self.__cost_price = cost_price

    def getName(self):
        """
        Returns the stock's name
        """
        return self.__name

    def getHistory(self):
        """
        Returns the history data
        """
        return self.__history

    def getCloseData(self):
        """
        Returns the 'close' column of the history data
        and computes the variation between the open and close values.
        """
        history = self.__history.copy()
        history['Variation'] = 10000 * (
            history['Close'] - history['Open'])/history['Close']
        history['Variation'] = history['Variation'].astype(int)/10000
        return history[['Close', 'Variation']]

    def getSupport(self):
        return

    def getResistance(self):
        return

    def getGain(self):
        """
        Returns the gain earns with the stock
        """
        return self.getQuantity()*(self.getCurrentValue()-self.getCostPrice())

    def buy(self, quantity, price):
        """
        Whenever the stock is bought, the price and the quantity is updated with the
        new quantiy and price
        """
        if not self.getOwned():
            self.setOwned(True)
            self.setQuantity(quantity)
            self.setCostPrice(price)
        else:
            self.setCostPrice((self.getQuantity()*self.getCostPrice() +
                               quantity * price)/(quantity+self.getQuantity()))
            self.setQuantity(quantity+self.getQuantity())
        return

    def sell(self, quantity):
        """
        Whenever the stock is sold, the quantity is updated with the
        new quantiy
        """
        if quantity > self.getQuantity():
            return None
        # sell all the stocks
        elif quantity == self.getQuantity():
            self.setOwned(False)
            self.setQuantity(0)
            self.setCostPrice(0)
        # stell part of the stocks
        else:
            self.setQuantity(self.getQuantity()-quantity)
        return

    def plot(self):
        """
        Plot the evolution of the stock's price among time
        """
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


stock = Stock(name, simulation_date)


stock.buy(2, 23.4)
stock.buy(4, 250)

print("getCloseData : ", stock.getCloseData())

print(stock.getGain())

print(stock.getDateValue('2010-01-20'))
