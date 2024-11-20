from src.utils import Utils
from src.preprocessing import Preprocessor
# Any other imports you want to add can be added here

if __name__ == "__main__":
    run_dir = "./run_dir"
    Utils.create_directories(run_dir=run_dir)
    # Any other code you want to run when the main.py file is executed

    # ? Changing the preprocessor_config values will change the preprocessing steps
    '''
    Default values are as follows
        "Normalizer": "MinMaxScaler",
        "Encoder": "OneHotEncoder",
        "excls_cols": ["CustomerID"],
        "categorical_cols": ['Gender'],
    '''
    Utils.preprocessor_config["Normalizer"] = "LogNormalizer"
    Utils.preprocessor_config["Encoder"] = "LabelEncoder"
    dataset = Utils.load_data()

    preprocessor = Preprocessor(dataset)

    #! the final preprocessed dataset is returned with the following line
    dataset_preprocessed = preprocessor.preprocess()

    # print(dataset_preprocessed.head())
    print("main.py executed successfully")
