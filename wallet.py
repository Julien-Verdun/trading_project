
class Wallet:

    def __init__(self, stocks, initial_account=3000):
        self.stocks_amount = 0
        for stock in stocks:
            self.stocks_amount += stock.getCostPrice()
        self.available_cash = initial_account - \
            self.stocks_amount  # argent disponible en cash

        self.virtual_account = initial_account
        self.last_account = initial_account
        self.stocks = stocks

    def update(self, date):
        self.stocks_amount = 0
        for stock in self.stocks:
            self.stocks_amount += stock.getQuantity()*stock.getDateValue(date)
        self.virtual_account = self.available_cash + self.stocks_amount

    def save_last_account(self):
        self.last_account = self.virtual_account

    def buying_autorisation(self, i, quantity, date):
        return self.available_cash > quantity * self.stocks[i].getDateValue(date)

    def sell(self, i, date):
        self.available_cash += self.stocks[i].getQuantity() * \
            self.stocks[i].getDateValue(date)

    def buy(self, i, date, quantity=1):
        self.available_cash -= quantity * self.stocks[i].getDateValue(date)
