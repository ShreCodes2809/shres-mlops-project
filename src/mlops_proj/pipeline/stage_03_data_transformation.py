from mlops_proj.config.configuration import ConfigurationManager
from mlops_proj.components.data_transformation import DataTransformation
from mlops_proj import logger

STAGE_NAME = "DATA_TRANSFORMATION"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting_data()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} stage has started! <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} has completed! <<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e