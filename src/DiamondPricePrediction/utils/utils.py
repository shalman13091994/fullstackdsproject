#model training
from src.DiamondPricePrediction.components.data_transformation import DataTransformation
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import numpy as np


# def save_object(filepath, obj):

#     dir = os.path.join(file_path)

#     os.makedirs(os.path.dirname(dir),  exist_ok =True)

#     with open(file_path, "wb") as file_obj:
#             pickle.dump(obj, file_obj)



def evaluating_scores(true, predict):
    # rmse = np.sqrt(mean_squared_error(true, predict)) # getting an error show 

    rmse = mean_squared_error(true, predict)
    r2_square = r2_score(true, predict)
    mse = mean_squared_error(true, predict)
    mae = mean_absolute_error(true, predict)
    return mae, rmse, r2_square, mse


# if __name__ == "__main__":
#     evaluating_scores(true, predict)
#     # save_object(filepath, obj)

