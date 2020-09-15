import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from model import LSTM
from prepare_data import Data, Dataset

stock = "MC.PA"

input_size = 4
output_size = 1
nb_neurons = 200
learning_rate = 0.001
nb_epochs = 150

output_path = "/Users/baptiste/Desktop/training"


class StockPrediction():

    def __init__(self, stock, time_window, batch_size, learning_rate=0.001):

        self.stock = stock
        self.time_window = time_window
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.input_size = 4
        self.output_size = 1
        self.nb_neurons = 200

        self.prepare_data()
        self.output = "/Users/baptiste/Desktop/training"


    def validate(self):

        self.lstm_model.eval()
        error = []
        loss_function = nn.MSELoss()
        it = iter(self.real_data_dataloader)
        real_data = next(it)
        loss = []
        for i, (x,_) in enumerate(self.testing_dataloader):
            try:
                with torch.no_grad():
                    pred = self.lstm_model(x.float())
                    pred = self.data.unnormalizeData(pred)
                    real_data = real_data.view(-1,1)
                    error = self.compute_error(error, pred, real_data)
                real_data = next(it)
            except:
                pass
        error_mean = np.mean(error) * 100
        print("Mean error percentage : ", error_mean)
        self.lstm_model.train()

    def compute_error(self, error, pred, target):
        
        for i in range(self.batch_size):
            error.append(abs(pred[i,0]-target[i,0])/target[i,0])
        return(error)


    def prepare_data(self):

        validation_split = 0
        test_split = 0.1
        train_split = 1 - validation_split - test_split


        self.data = Data(self.stock)
        df = self.data.getData()
        df_normalized = self.data.normalizeData(df)
        df_normalized = torch.FloatTensor(df_normalized.to_numpy())

        train_split = int(train_split*df.shape[0])
        validation_split = int(validation_split*df.shape[0])
        test_split = int(test_split*df.shape[0])

        training_split = df_normalized[:train_split,:]

        training_data = Dataset(training_split, self.time_window)
        self.training_dataloader = DataLoader(training_data, batch_size=self.batch_size)

        #testing_data
        real_data_tensor = torch.FloatTensor(df.to_numpy())
        self.real_data_test = torch.FloatTensor(real_data_tensor[-test_split:-self.time_window,3])
        testing_dataset = Dataset(df_normalized[-test_split:,:], self.time_window)
        self.testing_dataloader = DataLoader(testing_dataset, batch_size=self.batch_size)
        self.real_data_dataloader = DataLoader(self.real_data_test, batch_size=self.batch_size)

    def train(self):
        
        #Model
        self.lstm_model = LSTM(self.input_size, self.output_size, self.nb_neurons)
        self.lstm_model.load_state_dict(torch.load("/Users/baptiste/Desktop/training/AAPL_36.pth"))
        loss_function = nn.MSELoss()
        optimizer = torch.optim.Adam(self.lstm_model.parameters(), lr=self.learning_rate)
        print("Start training")
        for epoch in range(nb_epochs):
    
            for (x,y) in self.training_dataloader:

                optimizer.zero_grad()
                self.lstm_model.hidden_cell = (torch.zeros(1,self.batch_size,self.lstm_model.nb_neurons), torch.zeros(1,self.batch_size,self.lstm_model.nb_neurons))
                pred = self.lstm_model(x.float())
                y=y.view(self.batch_size, 1)
                loss = loss_function(pred, y)
                loss.backward()
                optimizer.step()

            print("epoch n°%s : loss = %s"%(epoch, loss.item()))
            self.validate()
            if epoch%5 == 1:
                model_name = "%s_%s.pth"%(self.stock, epoch)
                torch.save(self.lstm_model.state_dict(), os.path.join(output_path,model_name))

    def show_result(self):

        files = os.listdir(self.output)
        for file in files:
            if ".pth" in file:
                path = os.path.join(self.output, file)
                lstm_model = LSTM(self.input_size, self.output_size, self.nb_neurons)
                lstm_model.load_state_dict(torch.load(path))
                lstm_model.eval()
                print("model : %s loaded"%path)
                predictions = []

                for (x,_) in self.testing_dataloader:
                    if x.shape[0] == self.batch_size:
                        with torch.no_grad():
                            lstm_model.hidden_cell = (torch.zeros(1,self.batch_size,lstm_model.nb_neurons), torch.zeros(1,self.batch_size,lstm_model.nb_neurons))
                            output = lstm_model(x.float())
                            output = self.data.unnormalizeData(output).squeeze()
                            predictions+=output.tolist()
                
                plt.plot(predictions, label="prediction")
                plt.plot(self.real_data_test, label="target")
                plt.title(file)
                plt.legend()
                plt.show()


def main():

    stockprediction = StockPrediction(stock="AAPL", time_window=5, batch_size=5)
    #stockprediction.train()
    #stockprediction.show_result()




if __name__ == '__main__':
    main()
else:
    pass