import torch.nn as nn
import torch

class LSTM(nn.Module):

    def __init__(self, input_size, output_size, nb_neurons, batch=True):

        super().__init__()


        self.input_size = input_size
        self.output_size = output_size
        self.nb_neurons = nb_neurons

        self.lstm = nn.LSTM(self.input_size, self.nb_neurons, batch_first=batch)
        self.linear = nn.Linear(self.nb_neurons, self.output_size)
        self.hidden_cell = (torch.zeros(1,1,self.nb_neurons), torch.zeros(1,1,self.nb_neurons))
    

    def forward(self, input):
        
        output, self.hidden_cell = self.lstm(input, self.hidden_cell)
        pred = self.linear(output)
        return pred