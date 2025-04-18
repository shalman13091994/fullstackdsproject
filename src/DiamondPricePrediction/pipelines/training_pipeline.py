
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "src"))

from DiamondPricePrediction.components.data_ingestion import *
from DiamondPricePrediction.components.data_transformation import *
from DiamondPricePrediction.components.model_trainer import *
from DiamondPricePrediction.components.model_evaluation import *

from DiamondPricePrediction.utils.utils import evaluating_scores

data_ingestion = DataIngestion()
data_ingestion.initiate_dataingestion()

data_transformation = DataTransformation()
train_arr, test_arr = data_transformation.initiate_data_transformation()

model_trainer = ModelTrainer()
model_trainer.initiatemodeltraining(train_arr, test_arr)

# for the mflow and digshub
model_evaluat = model_evaluation()
model_evaluat.initiate_evaluation(train_arr, test_arr)

# to run the digshub model in the local to test the data
mlflowtest(train_arr, test_arr)