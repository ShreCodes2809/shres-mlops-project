import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path
from mlops_proj.utils.common import save_json
from mlops_proj.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config=ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2
    
    def mlflow_tracking(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        # setting a tracking URI for the remote server on dagshub
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            y_preds = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, y_preds)

            # saving the metrics locally
            scores = {"RMSE": rmse, "MAE": mae, "R2 SCORE": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("RMSE", rmse)
            mlflow.log_metric("MAE", mae)
            mlflow.log_metric("R2 SCORE", r2)

            # model registry does not work with the file store
            if tracking_url_type_store != "file":

                # register the model (for more info, visit this page: https://mlflow.org/docs/latest/ml/model-registry/)
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")