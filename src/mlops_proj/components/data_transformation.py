import os
from mlops_proj import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlops_proj.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config=DataTransformationConfig):
        self.config = config
    

    # In other projects, you can add different data transformation techniques such as PCA, Scalar and
    # all other different EDA techniques for in-depth data cleaning and analysis before passing this
    # data to the model

    def train_test_splitting_data(self):
        data = pd.read_csv(self.config.unclean_data_path)

        # split the data into training and testing datasets
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Split the data into training and testing datasets!")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)