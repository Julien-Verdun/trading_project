import os
import numpy as np
from matplotlib import pyplot as plt

import torch

from model import LSTM
from prepare_data import Data



def validate():

    stock = "MC.PA"
    directory = "/Users/baptiste/Desktop/training"

    input_size = 4
    output_size = 4
    nb_neurons = 200

    test_split = 0.1
    time_window = 5

    dataloader = Data(stock)
    df = dataloader.getData()
    real_data = df.to_numpy()
    df_normalized = dataloader.normalizeData(df)
    df_normalized = torch.FloatTensor(df_normalized.to_numpy())

    test_split = int(test_split*df.shape[0])
    real_test_split = real_data[-test_split:-time_window:,3]
    testing_split = df_normalized[-test_split:,:]

    files = os.listdir(directory)

    for file in files:
        if ".pth" in file:
            path = os.path.join(directory, file)
            lstm_model = LSTM(input_size, output_size, nb_neurons)
            lstm_model.load_state_dict(torch.load(path))
            print("model : %s loaded"%path)

            lstm_model.eval()

            predictions = []

            for i in range(testing_split.shape[0]-time_window):

                x_test = testing_split[i:i+time_window]

                with torch.no_grad():

                    lstm_model.hidden_cell = (torch.zeros(1,1,lstm_model.nb_neurons), torch.zeros(1,1,lstm_model.nb_neurons))
                    predictions.append(dataloader.unnormalizeData(lstm_model(x_test).tolist()))
            predictions = np.array(predictions)[:,3,0]
            
            #plt.figure(15,10)
            plt.plot(real_test_split, label="target")
            plt.plot(predictions, label="prediction")
            plt.title(file)
            plt.legend()
            plt.show()
        





if __name__ == '__main__':
    validate()
else:
    pass