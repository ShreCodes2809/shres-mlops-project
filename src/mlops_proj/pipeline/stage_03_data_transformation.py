from mlops_proj.config.configuration import ConfigurationManager
from mlops_proj.components.data_transformation import DataTransformation
from mlops_proj import logger

STAGE_NAME = "DATA_TRANSFORMATION"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open('artifacts.data_validation/status.txt', 'r') as f:
                status = f.read().split(":")[-1].strip()
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting_data()
            
            else:
                raise Exception("Your data schema is not valid!")
        
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} stage has started! <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} has completed! <<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e