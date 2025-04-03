# Data Transformation  - handling the missing value, seggreggating the category and numerical value, setting up the pipeline, preprocessors

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from src.DiamondPricePrediction.components.data_ingestion import *
from sklearn.impute import SimpleImputer
# from src.DiamondPricePrediction.utils.utils import save_object

from dataclasses import dataclass # this have __init__ method inside just to call as decorator
import os
import numpy as np
import joblib

# class DataTransformationConfig:
#     def __init__(self):
#         self.processor_obj_file_path = os.path.join(r'D:\Datascience\fullstackdsproject\artificats', 'preprocessor.pkl')


# class DataTransformation:

#     def __init__(self):
#         self.DataTransformationConfig = DataTransformationConfig()


#     def get_data_transformation(self):
        
#         data = pd.read_csv(r'D:\Datascience\fullstackdsproject\artificats\raw.csv')
#         #categorical_columns

#         # categorical_columns =data.select_dtypes(include=object).columns
#         # categorical_columns = list(categorical_columns)
#         # print(categorical_columns)
        
#         #numerical columns
#         # numerical_columns =data.select_dtypes(exclude=object).columns
#         # numerical_columns = numerical_columns.drop(['id'])
#         # numerical_columns = list(numerical_columns)
#         # print(numerical_columns)

#         #assign the ordinal encoding basis of the data which we have done already in Model_Training

#         logging.info('Data Transformation initiated')
            
#         # Define which columns should be ordinal-encoded and which should be scaled
#         categorical_cols = ['cut', 'color','clarity']
#         numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
#         # Define the custom ranking for each ordinal variable
#         cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
#         color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
#         clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
        
#         logging.info('Pipeline Initiated')
            
#             ## Numerical Pipeline
#         num_pipeline=Pipeline(
#                 steps=[
#                 ('imputer',SimpleImputer(strategy='median')),
#                 ('scaler',StandardScaler())

#                 ]

#             )
            
#             # Categorigal Pipeline
#         cat_pipeline=Pipeline(
#                 steps=[
#                 ('imputer',SimpleImputer(strategy='most_frequent')),
#                 ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
#                 ('scaler',StandardScaler())
#                 ]

#             )
            
#         preprocessor=ColumnTransformer([
#             ('num_pipeline',num_pipeline,numerical_cols),
#             ('cat_pipeline',cat_pipeline,categorical_cols)
#             ])
            
#         return preprocessor
            

            
            
        
#     # except Exception as e:
#     #         logging.info("Exception occured in the initiate_datatransformation")

#     #         raise customexception(e,sys)


#     def initiate_data_transformation(self):

#         # access the train n test data
#         train_df = pd.read_csv(r'D:\Datascience\fullstackdsproject\artificats\test.csv')
#         test_df = pd.read_csv(r'D:\Datascience\fullstackdsproject\artificats\test.csv')

#         preprocessing_obj = self.get_data_transformation()

#         #split the data into test and train 
         
#         target_column_name = 'price'
#         drop_columns = [target_column_name,'id']
            
#         # train_arr = [processed features + target]
#         input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
#         target_feature_train_df=train_df[target_column_name]
            
#         # test_arr = [processed features + target]
#         input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
#         target_feature_test_df=test_df[target_column_name]
        

#         #X train and X test
            
#         input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            
#         input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
        
 

#         # print(input_feature_train_arr)
#         # print(input_feature_test_df)

#         logging.info("Applying preprocessing object on training and testing datasets.")
        
#         #need to pass this as array 
#         train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
#         test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

#         # print(train_arr)

#         return(
#             train_arr,
#             test_arr
#         )

#         self.save_object(
#            filepath = self.DataTransformationConfig.processor_obj_file_path,
#            obj= preprocessing_obj
#         )

#         # np.save('artifacts/train_array.npy', train_arr)
#         # np.save('artifacts/test_array.npy', test_arr)

#         # train_arr = np.load('artifacts/train_array.npy')
#         # test_arr = np.load('artifacts/test_array.npy')

    
#     #Saves an object using pickle
#     def save_object(self, filepath, obj):
#         filepath = self.DataTransformationConfig.processor_obj_file_path,
#         obj= preprocessing_obj

#         dir = os.path.join(file_path)

#         os.makedirs(os.path.dirname(dir),  exist_ok =True)

#         with open(file_path, "wb") as file_obj:
#                 pickle.dump(obj, file_obj)

# if __name__ == "__main__":
#     DataTransformation = DataTransformation()
#     DataTransformation.get_data_transformation()
#     DataTransformation.initiate_data_transformation()
   

import os
import pickle
import logging
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


class DataTransformationConfig:
    def __init__(self):
        self.processor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def get_data_transformation(self):

        data = pd.read_csv(r'D:\Datascience\fullstackdsproject\artifacts\raw.csv')
#         #categorical_columns

#         # categorical_columns =data.select_dtypes(include=object).columns
#         # categorical_columns = list(categorical_columns)
#         # print(categorical_columns)
        
#         #numerical columns
#         # numerical_columns =data.select_dtypes(exclude=object).columns
#         # numerical_columns = numerical_columns.drop(['id'])
#         # numerical_columns = list(numerical_columns)
#         # print(numerical_columns)

 #assign the ordinal encoding basis of the data which we have done already in Model_Training

        logging.info('Data Transformation initiated')
            
        """Creates and returns a preprocessing pipeline."""
        logging.info('Data Transformation initiated')

        categorical_cols = ['cut', 'color', 'clarity']
        numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

        # Define category order for OrdinalEncoder
        cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
        color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
        clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

        logging.info('Pipeline Initiated')

        # Numerical Pipeline
        num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        # Categorical Pipeline
        cat_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('ordinalencoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
            ('scaler', StandardScaler())
        ])

        # Combine pipelines
        preprocessor = ColumnTransformer([
            ('num_pipeline', num_pipeline, numerical_cols),
            ('cat_pipeline', cat_pipeline, categorical_cols)
        ])

        return preprocessor

    def initiate_data_transformation(self):
        """Applies data transformation on train and test datasets and saves the preprocessor."""
        try:
            logging.info("Reading Train and Test Data")
            train_df = pd.read_csv(r'D:\Datascience\fullstackdsproject\artifacts\train.csv')
            test_df = pd.read_csv(r'D:\Datascience\fullstackdsproject\artifacts\test.csv')

            preprocessing_obj = self.get_data_transformation()

            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']

            # Separating input features and target variable
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            # Apply transformations
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")

            # Combine transformed features with target column
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # Save the preprocessor
            self.save_object(self.config.processor_obj_file_path, preprocessing_obj)

            return train_arr, test_arr

        except Exception as e:
            logging.error("Exception occurred in initiate_data_transformation", exc_info=True)
            raise e

    def save_object(self, file_path, obj):
        """Saves an object using pickle."""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, "wb") as file_obj:

                #due to scikit learn compatibilty issue in docker
                joblib.dump(obj, file_obj)

                # pickle.dump(obj, file_obj)

            logging.info(f"Object saved successfully at {file_path}")

        except Exception as e:
            logging.error("Error in saving object", exc_info=True)
            raise e


if __name__ == "__main__":
    transformer = DataTransformation()
    transformer.get_data_transformation()
    transformer.initiate_data_transformation()
