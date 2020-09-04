
class Wallet:

    def __init__(self, stocks, initial_account=3000):
        self.account = initial_account
        self.virtual_account = initial_account
        self.last_account = initial_account
        self.stocks = stocks

    # def update(self, date):
    #     self.last_account = self.account
    #     self.account = 0
    #     for stock in self.stocks:
    #         quantity = stock.getQuantity()
    #         price = stock.getDateValue(date)
    #         self.account += price * quantity

    def update(self, date):
        self.virtual_account = self.account
        for stock in self.stocks:
            self.virtual_account += stock.getGain(date)

    def save_last_account(self):
        self.last_account = self.virtual_account

    def sell(self, i, date):
        self.account += self.stocks[i].getGain(date)
