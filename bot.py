from stock import Stock
from strategy import Strategy
from wallet import Wallet


class Bot():

    def __init__(self, stocks_id):
        self.quantity = 1
        self.stocks_id = stocks_id

        self.stocks = [stock(stock_id) for stock_id in self.stocks_id]
        self.wallet = wallet(self.stocks)



    def run(self):
        """
        Run strategy and update wallet 
        """
        strats = Strategy(self.stocks)
                
        for i,strat in enumerate(strats):

            if strat == "buy":
                self.stocks[i].buy(self.quantity)
            
            elif strat == "sell":
                self.stocks[i].sell(self.quantity)

        self.wallet.update()


        

        
