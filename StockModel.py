import pandas as pd
import numpy
import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM 

class StockModel:

    """ builds the machine learning model.
        runs analysis on the past stock prices. then attempts to predict
        the future prices. 
    """
   
    def __init__(self, dataFrame):

       self.data = dataFrame.filter(["_close"]) # filter data to only include the closing price
       self.dataSet = self.data.values 
       self.scaledData = self.scaleData(self.dataSet)

       self.train_set_length = math.ceil(len(self.data) * 0.9) # 90% of the data to train
       self.test_set_length = math.ceil(len(self.data) * 0.1) # 10% of the data to test

       self.training_ds = self.scaledData[:self.train_set_length]
       self.test_ds = self.scaledData[self.test_set_length::-1]

    """ scales the data to elimiate anomolies caused 
        by greatly different values.
    """
    def scaleData(self, dataSet):
        scaler = MinMaxScaler(feature_range=(0,1))
        return  scaler.fit_transform(dataSet)
       


    def train(self):
        print(self.training_ds)
        print("\n\n")
        print(self.test_ds)

    def test(self):
        pass
        
    def runPrediction(self):  
        pass

    def writePrediction(self):
        pass

