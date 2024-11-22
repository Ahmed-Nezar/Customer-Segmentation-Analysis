import os
import pandas as pd


class Utils:

    preprocessor_config = {
        "Normalizer": "MinMaxScaler",
        "Encoder": "OneHotEncoder",
        "excls_cols": ["CustomerID"],
        "categorical_cols": ['Gender'],
        # "Imputer": "SimpleImputer",
        # "Imputer_strategy": "mean",
    }

    @classmethod
    def create_directories(self, run_dir: str):
        self.log_dir = os.path.join(run_dir, "logs")
        self.data_dir = os.path.join(run_dir, "data")
        self.data_path = os.path.join(self.data_dir, "dataset.csv")
        self.model_dir = os.path.join(self.log_dir, "models")
        self.plot_dir = os.path.join(self.log_dir, "plots")
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.model_dir, exist_ok=True)
        os.makedirs(self.plot_dir, exist_ok=True)
        # print(f"Created directories: {self.log_dir}, {self.data_path}, {self.model_dir}")
        # Any other directories you want to create can be added here

    @classmethod
    def load_data(self):
        """
        Load the dataset from the specified path in the configuration.
        Returns:
            pd.DataFrame: The dataset.
        """
        return pd.read_csv(self.data_path)
    
    @classmethod
    def get_dir(self):
        return self.log_dir, self.data_dir, self.model_dir, self.plot_dir 