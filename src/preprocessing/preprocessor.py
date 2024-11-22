import pandas as pd
import numpy as np
from src.utils import Utils


class Preprocessor:
    def __init__(self, dataset):
        """
        Initializes the Preprocessor class.

        Attributes:
            config (dict): Configuration settings for the preprocessor.
            dataset (pd.DataFrame): The dataset loaded from the specified CSV file.
        """
        self.config = Utils.preprocessor_config
        # self.dataset = pd.read_csv(Utils.data_path)
        self.dataset = dataset
        # self.Cat_columns = []

    def preprocess(self):
        """
        Preprocess the dataset by performing the following steps:
        1. Drop columns specified in the configuration.
        2. Scale the dataset.
        3. Encode categorical variables.

        Returns:
            pd.DataFrame: The preprocessed dataset.
        """
        # self.__check_nulls()
        # self.__check_duplicates()
        self.__drop_cols(self.config["excls_cols"])
        # self.__rename()
        # self.dataset = self.dataset.drop(columns=self.config["excls_cols"])
        if self.config["Normalizer"] and self.config["Normalizer"] != "None":
            self.__scale()
        self.__encode()
        return self.dataset

    def __drop_cols(self, col_list):
        """
        Drops specified columns from the dataset.
        Parameters:
        - col_list (list): List of column names to be dropped from the dataset.

        Returns:
            None
        """
        self.dataset = self.dataset.drop(columns=col_list)

    def __rename(self):
        """
        Renames specific columns in the dataset for consistency and ease of use.

        The following columns are renamed:
        - 'Annual Income (k$)' to 'Annual_Income'
        - 'Spending Score (1-100)' to 'Spending_Score'

        Returns:
            None
        """
        self.dataset = self.dataset.rename(columns={'Annual Income (k$)': 'Annual_Income',
                                                    'Spending Score (1-100)': 'Spending_Score'})

    def __scale(self):
        """
        Scales the numerical columns of the dataset based on the specified normalizer in the configuration.
        The method supports three types of normalizers:
        - MinMaxScaler: Scales features to a given range, usually between 0 and 1.
        - StandardScaler: Standardizes features by removing the mean and scaling to unit variance.
        - LogNormalizer: Custom normalizer that applies a logarithmic transformation.
        Raises:
            ValueError: If the specified normalizer in the configuration is not supported.
        Note:
            The columns specified in the configuration under "categorical_cols" are excluded from scaling.
        """
        if self.config["Normalizer"] == "MinMaxScaler":
            from sklearn.preprocessing import MinMaxScaler
            normalizer = MinMaxScaler()

        elif self.config["Normalizer"] == "StandardScaler":
            from sklearn.preprocessing import StandardScaler
            normalizer = StandardScaler()

        elif self.config["Normalizer"] == "LogNormalizer":
            # from src.preprocessing.preprocessor import LogNormalizer
            normalizer = LogNormalizer()

        else:
            raise ValueError(
                "Normalizer not supported, please choose from MinMaxScaler, StandardScaler or LogNormalizer")

        for col in self.dataset.columns:
            if col not in self.config["categorical_cols"]:
                self.dataset[col] = normalizer.fit_transform(
                    self.dataset[[col]])

    def __encode(self):
        """
        Encodes categorical columns in the dataset based on the specified encoder in the configuration.
        This method supports two types of encoders:
        1. OneHotEncoder: Converts categorical variables into a series of binary columns.
        2. LabelEncoder: Converts categorical variables into numeric labels.
        Raises:
            ValueError: If the specified encoder in the configuration is not supported.
        Note:
            The configuration dictionary (`self.config`) must contain:
            - "Encoder": A string specifying the encoder type ("OneHotEncoder" or "LabelEncoder").
            - "categorical_cols": A list of column names that are categorical and need encoding.
        Example:
            config = {
                "Encoder": "OneHotEncoder",
                "categorical_cols": ["gender", "country"]
            }
        """
        if self.config["Encoder"] == "OneHotEncoder":
            from sklearn.preprocessing import OneHotEncoder
            encoder = OneHotEncoder()
            for col in self.dataset.columns:
                if col in self.config["categorical_cols"]:
                    self.dataset = pd.get_dummies(
                        self.dataset, columns=[col], dtype=int)

        elif self.config["Encoder"] == "LabelEncoder":
            from sklearn.preprocessing import LabelEncoder
            encoder = LabelEncoder()
            for col in self.dataset.columns:
                if col in self.config["categorical_cols"]:
                    self.dataset[col] = encoder.fit_transform(
                        self.dataset[col])
        else:
            raise ValueError(
                "Encoder not supported, please choose from OneHotEncoder or LabelEncoder")

    def __check_nulls(self):
        """
        Checks for null values in the dataset.

        This method checks if there are any null values in the dataset. If null values are found,
        it prints "Nulls imputed". Otherwise, it prints "No nulls found".
        """
        if self.dataset.isnull().sum().sum() > 0:
            # self.__impute()
            print("Nulls imputed")
        else:
            print("No nulls found")

    def __check_duplicates(self):
        """
        Check for and remove duplicate rows in the dataset.

        This method checks if there are any duplicate rows in the dataset. If duplicates are found,
        they are removed, and a message indicating that duplicates were removed is printed. If no
        duplicates are found, a message indicating that no duplicates were found is printed.

        Returns:
            None
        """
        if self.dataset.duplicated().sum() > 0:
            self.dataset = self.dataset.drop_duplicates()
            print("Duplicates removed")
        else:
            print("No duplicates found")

# TODO: Can be moved to another folder if needed


class LogNormalizer():
    def _Log_Normalize(self, X):
        """
        Apply log normalization to the input data.

        This method takes an input array `X` and applies log normalization to it.
        The transformation is defined as sign(X) * log(abs(X) + 1), which helps in
        handling both positive and negative values and reducing the impact of large
        outliers.

        Parameters:
        X (numpy.ndarray): The input data array to be normalized.

        Returns:
        numpy.ndarray: The log-normalized data array.
        """
        return np.sign(X)*np.log(np.abs(X)+1)

    def fit_transform(self, X):
        """
        Fits the preprocessor to the data and transforms it.

        Parameters:
        X (pd.Series or np.ndarray): The input data to be transformed. If a pandas Series is provided, it will be converted to a numpy array.

        Returns:
        np.ndarray: The transformed data after applying log normalization.
        """
        if isinstance(X, pd.Series):
            X = X.to_numpy().reshape(-1, 1)
        return self._Log_Normalize(X)
