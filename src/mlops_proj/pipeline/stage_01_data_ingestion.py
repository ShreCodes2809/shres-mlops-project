from mlops_proj.config.configuration import ConfigurationManager
from mlops_proj.components.data_ingestion import DataIngestion
from mlops_proj import logger

STAGE_NAME = "DATA_INGESTION"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # initializing and creating the configuration object
        config = ConfigurationManager()

        # getting the data ingestion configuration from the "config.yaml" file
        data_ingestion_config = config.get_data_ingestion_config()

        # creating the data ingestion object
        data_ingestion = DataIngestion(config = data_ingestion_config)

        # downloading the dataset file using the object
        data_ingestion.download_file()

        # extracting the downloaded file at the target unzipping directory which was already mentioned in the configuration file
        data_ingestion.extract_zipfile()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} stage has started! <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} has completed! <<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e