import os 
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from src.datascience.entity.config__entity import ModelEvaluationConfig
from src.datascience.constants import *
from src.datascience.utils.common import read_yaml,create_directories,save_json

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config

    def eval_metric(self,actual,pred):
        rsme=np.sqrt(mean_squared_error(actual,pred))
        mae=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)
        return rsme,mae,r2

    def log_into_mlflow(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_data_path)

        test_x=test_data.drop([self.config.target_column],axis=1)
        test_y=test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities=model.predict(test_x)

            (rsme,mae,r2)=self.eval_metric(test_y,predicted_qualities)

            #saving metric as local
            scores={'rsme':rsme,'mae':mae,"r2":r2}
            save_json(path=Path(self.config.metric_file_name),data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric('rsme',rsme)
            mlflow.log_metric('r2',r2)
            mlflow.log_metric("mae",mae)


            #Model registry does not work with file store
            if tracking_url_type_store!="file":

                mlflow.sklearn.log_model(model,"model",registered_model_name="Elasticmodel")
            else:
                mlflow.sklearn.log_model(model,"model")
                