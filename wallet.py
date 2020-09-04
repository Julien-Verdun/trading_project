
class Wallet:

    def __init__(self, stocks, initial_account=3000):
        # self.account = initial_account

        self.stocks_amount = 0
        for stock in stocks:
            self.stocks_amount += stock.getCostPrice()
        self.available_cash = initial_account - \
            self.stocks_amount  # argent disponible en cash

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

    """
    verifier qu'il est possible d'acheter une action avant de le faire : montant action < available_cash
    quand on vend on transfere le montant vendu sur available_cash
    quand on achete on transfere l'argent sur stocks_amount
    on calcule avec le update a tout moment le bilan en faisant available_cash + somme sur action des quantites * montants
    """

    def update(self, date):
        # self.virtual_account = self.account
        self.stocks_amount = 0
        for stock in self.stocks:
            self.stocks_amount += stock.getDateValue(date)
        self.virtual_account = self.available_cash + self.stocks_amount

    def save_last_account(self):
        self.last_account = self.virtual_account

    def buying_autorisation(self, i, quantity, date):
        return self.available_cash > quantity * self.stocks[i].getDateValue(date)

    def sell(self, i, date):
        self.available_cash += self.stocks[i].getDateValue(date)
        # self.stocks_amount -= self.stocks[i].getDateValue(date)
        # self.account += self.stocks[i].getGain(date)

    def buy(self, i, date):
        self.available_cash -= self.stocks[i].getDateValue(date)
        # self.stocks_amount += self.stocks[i].getDateValue(date)
        # self.account += self.stocks[i].getGain(date)
