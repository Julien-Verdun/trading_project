from stock import Stock

class Walllet():

    def __init__(self, stocks):

        self.account = 0 
        self.stocks = stocks

    def update(self):

		for stock in self.stocks:
			quantity = stock.getQuantity()
			price = stock.getCurrentValue()

			self.account+= price * quantity

