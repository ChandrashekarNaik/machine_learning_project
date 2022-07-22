from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingestd_train_dir","ingestd_test_dir"])


DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path", "report_file_path", "report_page_file_path"])


DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
                                                                    "trannsformed_train_dir",
                                                                    "transformed_test_dir",
                                                                    "preprocessed_object_file_path"])


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path", "base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path", "time_stamp"])

ModelPusherConfig = namedtuple("ModelPushConfig",["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])

