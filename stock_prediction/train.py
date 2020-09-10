import pandas as pd
import os

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

def train():

    validation_split = 0
    test_split = 0.1
    train_split = 1 - validation_split - test_split
    time_window = 4
    BATCH_SIZE = 2

    #get Data
    dataloader = Data(stock)
    df = dataloader.getData()
    df_normalized = dataloader.normalizeData(df)
    df_normalized = torch.FloatTensor(df_normalized.to_numpy())

    print("Data loaded")

    #split data
    train_split = int(train_split*df.shape[0])
    validation_split = int(validation_split*df.shape[0])
    test_split = int(test_split*df.shape[0])

    training_split = df_normalized[:train_split,:]
    #validation_split = df_normalized[train_split:train_split+validation_split,:]
    #testing_split = df_normalized[train_split+validation_split:,:]

    training_data = Dataset(training_split, time_window)#dataloader.createDataloader(training_split, time_window)
    training_dataloader = DataLoader(training_data, batch_size=BATCH_SIZE)
    print("Data prepared")
    
    #Model
    lstm_model = LSTM(input_size, output_size, nb_neurons)
    loss_function = nn.MSELoss()
    optimizer = torch.optim.Adam(lstm_model.parameters(), lr=learning_rate)
    print("Start training")
    for epoch in range(nb_epochs):
  
        for (x,y) in training_dataloader:

            optimizer.zero_grad()
            lstm_model.hidden_cell = (torch.zeros(1,BATCH_SIZE,lstm_model.nb_neurons), torch.zeros(1,BATCH_SIZE,lstm_model.nb_neurons))

            pred = lstm_model(x.float())
            print(pred.shape)
            print(y.shape)
            return
            loss = loss_function(pred, y)
            loss.backward()
            optimizer.step()

        print("epoch n°%s : loss = %s"%(epoch, loss.item()))

        if epoch%5 == 1:
            model_name = "%s_%s.pth"%(stock, epoch)
            torch.save(lstm_model.state_dict(), os.path.join(output_path,model_name))






if __name__ == '__main__':
    train()
else:
    pass