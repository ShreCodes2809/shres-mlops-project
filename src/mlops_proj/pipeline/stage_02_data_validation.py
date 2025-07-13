from mlops_proj.config.configuration import ConfigurationManager
from mlops_proj.components.data_validation import DataValidation
from mlops_proj import logger

STAGE_NAME = "DATA_VALIDATION"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} stage has started! <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} has completed! <<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e