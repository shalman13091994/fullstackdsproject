import pandas as pd
import numpy as np 
import pyodbc
import sqlalchemy as sq
from sqlalchemy import create_engine
from sqlalchemy.engine import URL



from DiamondPricePrediction.exception import CustomException
from DiamondPricePrediction.logger import logging

#setting up the file path under the artificats
#always create a config
import os 
import pandas as pd
from sklearn.model_selection import train_test_split


class DataIngestionConfig:
    raw_data_path = os.path.join(r'artifacts', 'raw.csv')
    train_data_path = os.path.join(r'artifacts', 'train.csv')
    test_data_path = os.path.join(r'artifacts', 'test.csv')

   

class DataIngestion:


    def __init__(self):
        self.DataIngestionConfig = DataIngestionConfig()

    def initiate_dataingestion(self):
        try:

            #read the csv under the data folder
            data =pd.read_csv(r'D:\Datascience\fullstackdsproject\notebooks\data\gemstone.csv')
            print(data)

            #creating directory
            os.makedirs(os.path.dirname(os.path.join(self.DataIngestionConfig.raw_data_path)),exist_ok=True)

            #exporting to that raw data path
            data.to_csv((self.DataIngestionConfig.raw_data_path),index =False)

            #split the train n test data 
            train_data, test_data = train_test_split(data, test_size=0.33, random_state=42)

            train_data.to_csv((self.DataIngestionConfig.train_data_path),index =False)
            test_data.to_csv((self.DataIngestionConfig.test_data_path),index =False)


            return (

                self.DataIngestionConfig.raw_data_path,
                self.DataIngestionConfig.train_data_path,
                self.DataIngestionConfig.test_data_path

            )

        except Exception as e:
            print(f"error occured at {e}")

        print("Data ingestion completed")

# # Running the ingestion process - to test 
# if __name__ == "__main__":
#     ingestion = DataIngestion()
#     ingestion.initiate_dataingestion()