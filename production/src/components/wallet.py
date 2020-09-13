class Wallet:

    def __init__(self, stocks, initial_account=3000):
        self.stocks_amount = 0
        for stock in stocks:
            self.stocks_amount += stock.getCostPrice()
        self.available_cash = initial_account - \
            self.stocks_amount  # argent disponible en cash

        self.virtual_account = initial_account
        self.total_commission = 0
        self.total_transaction = 0
        self.last_account = initial_account
        self.stocks = stocks

    def initdata(self, wallet):
        self.virtual_account = wallet["virtual_account"]
        self.available_cash = wallet["available_cash"]
        self.stocks_amount = wallet["stocks_amount"]
        self.last_account = wallet["last_account"]
        self.total_commission = wallet["total_commission"]
        self.total_transaction = wallet["total_transaction"]
        return

    def update(self, date):
        self.stocks_amount = 0
        for stock in self.stocks:
            self.stocks_amount += stock.getQuantity()*stock.getDateValue(date)
        self.virtual_account = self.available_cash + self.stocks_amount

    def save_last_account(self):
        self.last_account = self.virtual_account

    def buying_autorisation(self, i, quantity, date):
        # enough to cash buy stock's quantity, taking commissions into account
        return self.available_cash > quantity * (self.stocks[i].getDateValue(date) * (1 + self.stocks[i].getPropCommission()) + self.stocks[i].getFixedCommission())

    def sell(self, i, date):
        """
        This method is called when the bot sells i stocks. The commission is updated and
        the available cash is diminished (money is moved from available cash acount to stock account)
        """
        self.total_commission += self.stocks[i].getQuantity() * (self.stocks[i].getDateValue(
            date) * self.stocks[i].getPropCommission() + self.stocks[i].getFixedCommission())
        self.available_cash += self.stocks[i].getQuantity() * (self.stocks[i].getDateValue(
            date) * (1 - self.stocks[i].getPropCommission()) - self.stocks[i].getFixedCommission())
        self.total_transaction += 1

    def buy(self, i, date, quantity=1):
        """
        This method is called when the bot buys i stocks. The commission is updated and
        the available cash is increased (money is moved from stock account to available cash acount)
        """
        self.total_commission += self.stocks[i].getQuantity() * (self.stocks[i].getDateValue(
            date) * self.stocks[i].getPropCommission() + self.stocks[i].getFixedCommission())
        self.available_cash -= quantity * (self.stocks[i].getDateValue(date) * (
            1 + self.stocks[i].getPropCommission()) + self.stocks[i].getFixedCommission())
        self.total_transaction += 1
