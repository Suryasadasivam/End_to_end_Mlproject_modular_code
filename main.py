from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evalution_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME="DATA Ingestion Stage"
try:
    logger.info(f">>>>stage{STAGE_NAME}started<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>stage{STAGE_NAME}completed<<<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"
try:
        logger.info(f">>>>stage{STAGE_NAME}started<<<<<<")
        data_vald=DataValidationTrainingPipeline()
        data_vald.initiate_data_validation()
        logger.info(f">>>stage{STAGE_NAME}completed<<<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data Transformation Stage"
try:
        logger.info(f">>>>stage{STAGE_NAME}started<<<<<<")
        data_trans=DataTransformationTrainingPipeline()
        data_trans.initiate_data_transformation()
        logger.info(f">>>stage{STAGE_NAME}completed<<<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model Trainer Stage"
try:
        logger.info(f">>>>stage{STAGE_NAME}started<<<<<<")
        model_train=ModelTrainerTrainingPipeline()
        model_train.initiate_model_training()
        logger.info(f">>>stage{STAGE_NAME}completed<<<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model evaluation Stage"
try:
        logger.info(f">>>>stage{STAGE_NAME}started<<<<<<")
        model_eval=ModelEvaluationTrainingPipeline()
        model_eval.initiate_model_evaluation()
        logger.info(f">>>stage{STAGE_NAME}completed<<<<<<\n\nx=======x")
except Exception as e:
        logger.exception(e)
        raise e



