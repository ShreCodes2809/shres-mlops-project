import os
from pathlib import Path
from mlops_proj import logger
from urllib.request import urlretrieve
import zipfile
from mlops_proj.utils.common import get_size
from mlops_proj.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config = DataIngestionConfig):
        self.config = config
    

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! Here's info about the file: \n {headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    

    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)