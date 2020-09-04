
class Wallet:

    def __init__(self, stocks):
        self.account = 0
        self.last_account = 0
        self.stocks = stocks

    def update(self, date):
        self.last_account = self.account
        self.account = 0
        for stock in self.stocks:
            quantity = stock.getQuantity()
            price = stock.getDateValue(date)
            self.account += price * quantity
