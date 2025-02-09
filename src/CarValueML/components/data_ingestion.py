import sys
import os
import pandas as pd

from src.CarValueML.logger import logging
from src.CarValueML.exception import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join('artifacts', 'raw_data.csv')
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

        if not os.path.exists(self.ingestion_config.raw_data_path):
                raise Exception("Raw data file doesn't exist")

    def initiate_data_ingestion(self):
        try:
            data = pd.read_csv('data/data_preprocessed.csv')
            logging.info("Read data as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            logging.info("Creating artifacts folder")

            data.to_csv(self.ingestion_config.raw_data_path)

            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path)
            test_set.to_csv(self.ingestion_config.test_data_path)

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
          raise CustomException(e, sys)