
from stock_prediction.prepare_data import Data
from stock_prediction.model import LSTM

import torch



class StrategyML():

    def __init__(self, stocks, date, available_cash):
        self.stocks = stocks
        self.date = date
        self.available_cash = available_cash

        self.model_path = "/Users/baptiste/Desktop/training/final_model.pth"

        self.time_window = 6
        self.datatool = Data("")

    def run(self):

        orders = []

        for stock in self.stocks:

            #collect data
            stock_data = stock.getFullHistoryToDate(self.date, self.time_window)
            #normalize
            normalize_data = torch.FloatTensor(self.datatool.normalizeData(stock_data).to_numpy())

            input_data = torch.unsqueeze(normalize_data, 0)

            lstm_model = LSTM(4, 1, 200)
            lstm_model.load_state_dict(torch.load(self.model_path))
            lstm_model.eval()

            with torch.no_grad():

                lstm_model.hidden_cell = (torch.zeros(1,1,200), torch.zeros(1,1,200))
                output = lstm_model(input_data.float())
                prediction = self.datatool.unnormalizeData(output).squeeze().item()
                current_value = stock.getDateValue(self.date)
                stock_quantity = int(stock.getQuantity())
                
                diff = (current_value - prediction)/current_value

                if diff < -0.03 and stock_quantity > 0:
                    orders.append(("sell", int(stock_quantity)))
                elif diff > 0 and stock_quantity == 0:
                    orders.append(("buy", 1))
                elif diff > 0.1:
                    orders.append(("buy", 1))
                else:
                    orders.append("nogo")

        return orders



