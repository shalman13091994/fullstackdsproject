#model training
from src.DiamondPricePrediction.components.data_transformation import DataTransformation
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.DiamondPricePrediction.utils.utils import evaluating_scores


import numpy as np
from dataclasses import dataclass
import os
import pickle
import joblib


@dataclass # using this dataclass we dont have to manually initialise the init  method
class ModelTrainerConfig:

    modeltrainer_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.ModelTrainerConfig = ModelTrainerConfig()

    #to save the best model - declaring here to use this method inside the initiatemodeltraining method
    def save_object(self, file_path, obj):
        """Saves an object using pickle."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            
            #  due to scikit learn compatibilty issue in docker scikit learn pickle is not working
            joblib.dump(obj, file_obj)

            # pickle.dump(obj, file_obj)
        print(f"✅ Model saved at: {file_path}")
    
    
    def initiatemodeltraining(self, train_array, test_array):
         

        model_list =[]
        r2_list = []
        
        #to find the best model
        best_model = None
        best_r2 = -float("inf") # Start with the lowest possible R² score
        print(best_r2)
 

        #it will have both independent and target feature so splitting out  
        # train_array and test_array from the data_transformation.initiate_data_transformation()
        X_train, y_train, X_test, y_test = (
            train_array[:,:-1],
            train_array[:, -1], 
            test_array[:, :-1], 
            test_array[:, -1]
        )
        
  

        # print(train_array)

        # print(train_array[:,:-1])


        models ={
            'linear':LinearRegression(),
            'Ridge':Ridge(),
            'Lasso':Lasso(),
            'ElasticNet':ElasticNet()
        }

        
        for i in range(len(list(models))):
            
            model = list(models.values())[i]
            # print(model)
            model.fit(X_train, y_train)
            y_predict = model.predict(X_test)
            print("training score", model.score(X_train, y_train))

            #validation part 
            mae, rmse, r2_square, mse = evaluating_scores(y_predict, y_test)
            print(model)
            model_list.append(model)
            
            print("Model Training Performance")
            print("RMSE:", rmse)
            print("MAE:", mae)
            print("MSE:", mse)
            print(f"R² Score: {r2_square * 100:.2f}%")
            r2_list.append(r2_square)
            print('='*35)

            if r2_square > best_r2:
                best_r2 = r2_square
                best_model = model

        
        if best_model:

            print(f"\n✅ Best Model Saved: {best_model} with R² Score: {best_r2*100}")
            # self.save_object(self.ModelTrainerConfig.modeltrainer_file_path, best_model) #this will save as model.pkl

            #overriding the default model name with the dynamic model name 
            model_file_path = os.path.join('artifacts', f"{best_model}.pkl")

            self.save_object(model_file_path, best_model)




    # to save the best model
    

            

    
           
            


    

#     def evaluating_scores(true, predict):
#         # rmse = np.sqrt(mean_squared_error(true, predict)) # getting an error show 

#         rmse = mean_squared_error(true, predict)
#         r2_square = r2_score(true, predict)
#         mse = mean_squared_error(true, predict)
#         mae = mean_absolute_error(true, predict)
#         return mae, rmse, r2_square, mse


# if __name__=="__main__":
#     ModelTrainer = ModelTrainer()
#     data_transformation = DataTransformation()
#     train_array, test_array = data_transformation.initiate_data_transformation()  
#     ModelTrainer.initiatemodeltraining(train_array, test_array)



