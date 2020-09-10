import numpy as np
import sklearn
import sklearn.preprocessing
import pandas as pd
import pandas_datareader.data as web

import torch
from torch.utils.data import Dataset




class Data():

    def __init__(self, stock_id):

        self.stock_id = stock_id 

    def getData(self):
        df = web.DataReader(self.stock_id, data_source='yahoo', start='2000-01-01', end='2020-09-01')
        df = df[["High", "Low", "Open", "Close"]].dropna()
        return df 
    
    def normalizeData(self, df):
        df_norm = df.copy()
        self.normalizer = sklearn.preprocessing.MinMaxScaler()
        df_norm["High"] = self.normalizer.fit_transform(df.High.values.reshape(-1,1))
        df_norm["Low"] = self.normalizer.fit_transform(df.Low.values.reshape(-1,1))
        df_norm["Open"] = self.normalizer.fit_transform(df.Open.values.reshape(-1,1))
        df_norm["Close"] = self.normalizer.fit_transform(df.Close.values.reshape(-1,1))

        return df_norm

    def unnormalizeData(self, data):

        real_data = self.normalizer.inverse_transform(np.array(data).reshape(-1,1))
        return real_data

    def createDataloader(self, input_data, time_window):
        data =[]
        n = len(input_data)

        for i in range(n-time_window):
            seq = input_data[i:i+time_window]
            label = input_data[i+time_window, 3]
            data.append((seq,label))
        
        return data


        
class Dataset(Dataset):

    def __init__(self, data, time_window):

        self.data = data
        self.time_window = time_window

    def __getitem__(self, index):
        x = self.data[index:index+self.time_window]
        y = self.data[index+self.time_window,3]
        return x,y
    
    def __len__(self):
        return(len(self.data)-self.time_window)
        