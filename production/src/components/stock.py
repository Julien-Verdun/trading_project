import yfinance as yf
import time
import matplotlib.pyplot as plt
import numpy as np
from ..utils.time_utils import *


class Stock:
    """
    This class allows to get data from the stock market
    with an API
    """

    def __init__(self, name, date, fixed_commission,
                 prop_commission, moving_window, decrease_window, quantity=0):
        self.__name = name
        self.__owned = True
        self.__quantity = quantity
        self.__cost_price = 0
        # in euros
        self.__fixed_commission = fixed_commission
        # rate, proportionnal to stock price
        self.__prop_commission = prop_commission
        # parameters
        self.__decrease_window = decrease_window
        self.__moving_window = moving_window

        self.__stock = yf.Ticker(name)
        # print(increase_date(date, -(moving_window + decrease_window)))

        self.__history = self.__stock.history(
            start=increase_date(date, -(moving_window + decrease_window)),
            end=increase_date(date, -1)
        )
        self.__historical_data = self.getCloseData()
        return

    def initdata(self, stock):
        self.__quantity = stock["quantity"]
        self.__cost_price = stock["cost_price"]
        return

    def show(self, date):
        i = 0
        while self.getDateValue(increase_date(date, -i)) == None:
            i += 1

        return "\n----------Stock " + self.__name + "----------\nQuantity : " + str(self.__quantity) + \
            "\nPrice : " + str(self.__cost_price) + \
            "\nInitial price : " + str(self.getDateValue(increase_date(date, -i))) + \
            "\nPrice difference : " + str(self.getQuantity()*(self.getDateValue(
                increase_date(date, -i))-self.__cost_price)) + " euros\n"

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

    def getDateValue(self, date):
        """
        Returns the value of the 'close' value for date "date" (format year - month - day)
        """
        if date in self.__history.index:
            return self.__history['Close'][date]
        else:
            return None

    def getDateVariation(self, date):
        """
        Returns the value of the 'variation' value for date "date" (format year - month - day)
        """
        if date in self.__history.index:
            return self.__historical_data['Variation'][date]
        else:
            # print("!!!!!!!!!!!!!!!!!!!", date)
            return None

    def getMeanVariation(self, date):
        """
        Returns the mean value of the stock variation on a moving_window period before date
        """
        mean_var = 0
        for i in range(len(self.__historical_data["Variation"].tolist())):
            if self.__historical_data.index[i].timestamp() <= time.mktime(time.strptime(date, "%Y-%m-%d")):
                if (time.mktime(time.strptime(date, "%Y-%m-%d"))-self.__historical_data.index[i].timestamp()) / (24 * 3600) <= self.__moving_window:
                    mean_var += 100 * \
                        self.__historical_data["Variation"].tolist()[i]
            else:
                break
        return np.mean(mean_var)

    def getRSI(self, date, nb_days):
        historical_data = self.getHistoryToDate(date, nb_days)
        pos_var, neg_var = [], []
        # Calculation of the RSI
        for i in range(len(historical_data["Variation"].tolist())):
            if historical_data["Variation"].tolist()[i] > 0:
                pos_var.append(
                    historical_data["Variation"].tolist()[i])
                neg_var.append(0)
            else:
                neg_var.append(historical_data["Variation"].tolist()[i])
                pos_var.append(0)
        avg_gain, avg_loss = abs(np.mean(pos_var)), abs(np.mean(neg_var))
        return 100 * avg_gain / (avg_gain + avg_loss)

    def getStoch(self, date, nb_days):
        historical_data = self.getHistoryToDate(date, nb_days)
        close_values = historical_data["Variation"].tolist()
        last_close = close_values[-1]
        return 100 * ((last_close - min(close_values)) / (max(close_values) - min(close_values)))

    def isDecreasingStock(self, date):
        """
        Returns wheter or not the stock price is decreasing since a least "decrease_window"
        days and just increased at date "date"
        """
        i = 0
        j = 0
        while i <= self.__decrease_window:
            if self.getDateVariation(increase_date(date, -i-j-1)) != None:
                if self.getDateVariation(increase_date(date, -i-j-1)) > 0:
                    return False
                i += 1
            else:
                j += 1
        i = 0
        while self.getDateVariation(increase_date(date, -i)) == None:
            i += 1
        return self.getDateVariation(increase_date(date, i)) > 0

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

    def getFixedCommission(self):
        return self.__fixed_commission

    def getPropCommission(self):
        return self.__prop_commission

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

    def getHistoryToDate(self, date, nb_days):
        """
        Returns the nb_days last lines for a given date. For example, if I need the 5 last days to calculate smth
        getHistoryToDate(now, 5) will extract the 5 last entry
        """
        return self.__historical_data.loc[increase_date(date, - nb_days):date]

    def getSupport(self):
        return

    def getResistance(self):
        return

    def getGain(self, date):
        """
        Returns the gain earns with the stock
        """
        return self.getQuantity()*(self.getDateValue(date)-self.getCostPrice())

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

    def sell(self, quantity=None):
        """
        Whenever the stock is sold, the quantity is updated with the
        new quantiy
        """
        if quantity == None or quantity > self.getQuantity():
            return None
        # sell all the stocks
        elif quantity == self.getQuantity():
            self.setOwned(False)
            self.setQuantity(0)
            self.setCostPrice(0)
        # stell part of the stocks
        else:
            self.setQuantity(self.getQuantity()-quantity)
        return "sold"

    def plot(self):
        """
        Plot the evolution of the stock's price among time
        """
        plt.figure()
        plt.plot(self.__historical_data["Close"], '--*')
        plt.plot(self.getHistory().index, [self.getCostPrice(
        ) for k in range(len(self.getHistory().index))], '-')
        plt.title(self.getName() + " : Stock evolution")
        plt.xlabel("Date")
        plt.ylabel("Price ($) ")
        plt.show()
