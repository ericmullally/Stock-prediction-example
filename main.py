import sys
from json import loads
import pandas as pd
import StockModel


def main():
    #print("r")
    createModel()


def createModel():
    try:

        with open("textFiles/data.txt") as prices:
            data = loads(prices.readline())
            df = pd.DataFrame(data)

            newModel = StockModel.StockModel(df)
            
            newModel.train()

    except FileNotFoundError as err:
        print(f"{err.filename} not found")


def saveModel(model):
    pass


if __name__ == "__main__":
   main()