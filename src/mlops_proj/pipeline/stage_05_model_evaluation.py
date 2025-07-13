from mlops_proj.config.configuration import ConfigurationManager
from mlops_proj.components.model_evaluation import ModelEvaluation
from mlops_proj import logger

STAGE_NAME = "MODEL_EVALUATION_STAGE"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.mlflow_tracking()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} stage has started! <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} has completed! <<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e