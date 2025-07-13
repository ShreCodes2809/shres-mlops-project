from mlops_proj import logger
from mlops_proj.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlops_proj.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlops_proj.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlops_proj.pipeline.stage_04_model_trainer import ModelTrainingPipeline

STAGE_NAME_1 = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME_1} stage has started! <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>{STAGE_NAME_1} has completed! <<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_2 = "Data Validation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME_2} stage has started! <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>{STAGE_NAME_2} has completed! <<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_3 = "Data Transformation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME_3} stage has started! <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>{STAGE_NAME_3} has completed! <<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_4 = "Model Training Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME_4} stage has started! <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>{STAGE_NAME_4} has completed! <<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e