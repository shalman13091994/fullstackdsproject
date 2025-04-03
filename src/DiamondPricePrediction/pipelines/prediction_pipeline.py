from src.DiamondPricePrediction.components import *
import os 
import sys
import pandas as pd
import os, pickle 
import sys
from src.DiamondPricePrediction.components import *
from src.DiamondPricePrediction.utils.utils import *

class PredictPipeline:
    def __init__(self):
        pass

    def predict_data(self, features):
       
        # works on the local but aws it gives error so it has to give in below approach
    #    preprocessor_path =  os.path.join(r"D:\Datascience\fullstackdsproject\artifacts\preprocessor.pkl")
    #    model_path =  os.path.join(r"D:\Datascience\fullstackdsproject\artifacts\model.pkl")

       # Get base directory dynamically (works in AWS)
       BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

        # Use relative paths instead of absolute Windows paths
       preprocessor_path = os.path.join(BASE_DIR, "artifacts", "preprocessor.pkl")
       model_path = os.path.join(BASE_DIR, "artifacts", "model.pkl")
            
       preprocessor = load_object(preprocessor_path)
       model = load_object(model_path)
       
       #preprocessing
       scaled_data = preprocessor.fit_transform(features)
       predict = model.predict(scaled_data)

      #created a dataframe for the predicted price column 
       predict_price= pd.DataFrame(predict, columns=['predicted price(target)'])
        
       return predict_price


#creating a class for passing the parameters which is independent variable

# Creating a class for passing the parameters which are independent variables
class CustomData:
    def __init__(self, carat: float,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float,
                 cut: str,
                 color: str,
                 clarity: str):

        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_as_dataframe(self):
        """Creates and returns a DataFrame from the object's attributes."""
        create_dict = {
            'carat': [self.carat],
            'depth': [self.depth],
            'table': [self.table],
            'x': [self.x],
            'y': [self.y],
            'z': [self.z],
            'cut': [self.cut],
            'color': [self.color],
            'clarity': [self.clarity],
        }

        df = pd.DataFrame(create_dict)

        return df  # Ensure the DataFrame is returned

# if __name__ == '__main__': 
#     custom_data = CustomData(2.01, 58.7, 58.0, 8.2, 8.17, 4.82, "Premium", "I", "SI2")  # Instance
#     df = custom_data.get_as_dataframe()  # Store the returned DataFrame
#     print(df)  # Print the DataFrame

class CustomDataUpload:
    def __init__(self):
        pass
    def get_as_dataframe(self, filepath):
        
        df = pd.read_csv(filepath)

        # df = pd.read_csv(r"D:\Datascience\fullstackdsproject\notebooks\data\playground-series-s3e8\train.csv")
        return df # Ensure the DataFrame is returned