from mlops_proj import logger
from mlops_proj.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} stage has started! <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>{STAGE_NAME} has completed! <<<<<<\n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e