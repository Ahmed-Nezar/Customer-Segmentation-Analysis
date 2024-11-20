import pandas as pd
from src.utils import Utils

class Preprocessor:
    def __init__(self):
        self.config = Utils.preprocessor_config
        self.dataset = pd.read_csv(Utils.data_path)

    def preprocess(self):
        
        self.__check_nulls()
        self.__check_duplicates()

        self.__scale()
        self.__encode()
        return self.dataset
    
    def __check_nulls(self):
        if self.dataset.isnull().sum().sum() > 0:
            self.__impute()
            print("Nulls imputed")
        else:
            print("No nulls found")

    def __check_duplicates(self):
        if self.dataset.duplicated().sum() > 0:
            self.dataset = self.dataset.drop_duplicates()
            print("Duplicates removed")
        else:
            print("No duplicates found")

    def __impute(self):
        if self.config["Imputer"] == "SimpleImputer":
            from sklearn.impute import SimpleImputer
            imputer = SimpleImputer(strategy=self.config["Imputer_strategy"])
        else:
            raise ValueError("Imputer not supported")
        
        self.dataset = imputer.fit_transform(self.dataset)
        
    def __scale(self):
        if self.config["Normalizer"] == "MinMaxScaler":
            from sklearn.preprocessing import MinMaxScaler
            normalizer = MinMaxScaler()
            
        elif self.config["Normalizer"] == "StandardScaler":
            from sklearn.preprocessing import StandardScaler
            normalizer = StandardScaler()
        else:
            raise ValueError("Normalizer not supported")
        
        self.dataset = normalizer.fit_transform(self.dataset)

    def __encode(self):
        if self.config["Encoder"] == "OneHotEncoder":
            from sklearn.preprocessing import OneHotEncoder
            encoder = OneHotEncoder()
        elif self.config["Encoder"] == "LabelEncoder":
            from sklearn.preprocessing import LabelEncoder
            encoder = LabelEncoder()
        else:
            raise ValueError("Encoder not supported")
        
        self.dataset = encoder.fit_transform(self.dataset)

