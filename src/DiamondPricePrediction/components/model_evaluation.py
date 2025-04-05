from urllib.parse import urlparse
from src.DiamondPricePrediction.components.data_transformation import DataTransformation
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import pandas as pd
import numpy as np
import mlflow, os
from src.DiamondPricePrediction.utils.utils import evaluating_scores, load_object
import dagshub

class model_evaluation:
    def __init__(self):
        pass

    def evaluate_metrics(self, actual, predict):  #y, yhat
        r2 = r2_score(actual, predict)
        mae = mean_absolute_error(actual, predict)
        mse = np.sqrt(mean_squared_error(actual, predict))# here is RMSE
        return mse, mae, r2


    def initiate_evaluation(self, train_arr, test_arr):
       
     
       # load the data
        X_train, y_train, X_test, y_test = (
            train_arr[:,:-1],
            train_arr[:, -1], 
            test_arr[:, :-1], 
            test_arr[:, -1]
        )

        #load the model
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

        model_path = os.path.join(BASE_DIR, "..", "artifacts", "linearRegression().pkl")

        model  = load_object(model_path)

        # dagshub uri - with digshub it will store in the digshub repo
        mlflow.set_registry_uri('https://dagshub.com/shalman13091994/fullstackdsproject.mlflow')
        
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        print(tracking_url_type_store) # output would be file n save it in digshub
        
        # will get under the remote -->experiments --> using mlflow tracking
        dagshub.init(repo_owner='shalman13091994', repo_name='fullstackdsproject', mlflow=True)


            
       #logging with the mlflow in local
        with mlflow.start_run():
        # will pass only the test data/validated data
            y_predict = model.predict(X_test)
            mse, mae, r2 = self.evaluate_metrics(y_test, y_predict)
            mlflow.log_metric("mse", mse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2_score", r2)
            mlflow.set_tag("model evaluation info", "Basic LR model for gemstone data from kaggle")

           # this condition is for the dagshub
                # Model registry does not work with file store
            if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
              
            else:
                    #save in local directory
                    mlflow.sklearn.log_model(model, "model")
           



if __name__ == "__main__":
    model_eval = model_evaluation()
    data_transformer = DataTransformation()  # <-- ✅ not same as class name
    train_array, test_array = data_transformer.initiate_data_transformation()
    model_eval.initiate_evaluation(train_array, test_array)





       


    