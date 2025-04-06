from urllib.parse import urlparse
from src.DiamondPricePrediction.components.data_transformation import DataTransformation
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import pandas as pd
import numpy as np
import mlflow, os
from src.DiamondPricePrediction.utils.utils import evaluating_scores, load_object
import dagshub

from mlflow.models.signature import infer_signature


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
            mlflow.set_tag("model evaluation info", "Basic LR model for gemstone data from kaggle") #till here it will log the experiements without models
            

        # for dagshub with the small dataframe for testing     
        # Assuming X_test is your input and model is trained
        
        input_example = X_test[:1]  # or create a small DataFrame with same columns
        prediction_example = model.predict(input_example)

            # Automatically generate the signature
        signature = infer_signature(input_example, prediction_example)

            # Log the model with metadata to the local mlrun 
        mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model",
                input_example=input_example,
                signature=signature
            )

        #     #save model to the local mlrun 
        # mlflow.sklearn.log_model(model, "model") # it will save the model under mlrun without any input data

        #    this condition is for the dagshub
                # Model registry does not work with file store
        if tracking_url_type_store != "file":

                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow

                mlflow.sklearn.log_model(
                    sk_model=model,
                    artifact_path="model",
                    input_example=input_example,
                    signature=signature, 
                    # registered_model_name="ml_model" # not registering due to under log_model
                    )
                     

                

                    # mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
              
        else:
                    #save in local directory
                    mlflow.sklearn.log_model(model, "model")

        # Register the model manually -- this s only working
        run_id = mlflow.active_run().info.run_id
        model_uri = f"runs:/{run_id}/model"
        result = mlflow.register_model(model_uri=model_uri, name="ml_model")


       #additional part for learning MLflow 
        from mlflow.tracking import MlflowClient

        client = MlflowClient()

        #2. Promote the model to "Staging" or 'production'
        model_level = client.transition_model_version_stage(
            name="ml_model",
            version=result.version,
            stage="Staging",  # or "Production"
            archive_existing_versions=True  # archive older prod/staging if exists
        )
        print("model_level--",model_level)

        # 3. Add description or comments to model version  - for the registered model
        model_version = client.update_model_version(
            name="ml_model",
            version=result.version, #for the version-specific
            
            description="Linear Regression model trained on diamond price dataset (v1)"
        )

        print("model_version--",model_version)


        # 📥 4. Load latest Production model from registry
        # Once promoted, you can pull it from any environment:
        from mlflow.sklearn import load_model

        model = load_model("models:/ml_model/Staging")  # production Or Staging


        # # 📋 5. List all registered models
        # models = client.list_registered_models()
        # for model in models:
        #     print(f"Model Name: {model.name}")


        # ✅ 6. Get all versions of a model
        versions = client.search_model_versions("name='ml_model'")
        for v in versions:
            print(f"Version: {v.version}, Stage: {v.current_stage}, Run ID: {v.run_id}")








if __name__ == "__main__":
    model_eval = model_evaluation()
    data_transformer = DataTransformation()  # <-- ✅ not same as class name
    train_array, test_array = data_transformer.initiate_data_transformation()
    model_eval.initiate_evaluation(train_array, test_array)




#testing the dagshubflow model with the data 

import mlflow
import pandas as pd

def mlflowtest(train_arr, test_arr):

    #will get this from the digshub under the artificats -->model -->path
    logged_model = 'runs:/35a1f3e8516a407096cf20c59cef1c41/model' 

    # Load model as a PyFuncModel
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    # Unpack data
    X_train, y_train, X_test, y_test = (
        train_arr[:, :-1],
        train_arr[:, -1], 
        test_arr[:, :-1], 
        test_arr[:, -1]
    )


    X_test_df = pd.DataFrame(X_test)
    # Predict
    predictions = loaded_model.predict(X_test_df)
    
    # Combine into a result DataFrame
    result_df = X_test_df.copy()
    result_df['Actual'] = y_test
    result_df['Predicted'] = predictions

    # Save
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    output_path = os.path.join(BASE_DIR, "..", "artifacts", "digshub_output_with_prediction.csv")

    result_df.to_csv(output_path, index=False)
    print(result_df.head())

if __name__ == "__main__":
    from src.DiamondPricePrediction.components.data_transformation import DataTransformation
    data_transformation = DataTransformation()
    train_arr, test_arr = data_transformation.initiate_data_transformation()
    mlflowtest(train_arr, test_arr)

       


    