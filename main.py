from src.utils import Utils, Monitor
from src.preprocessing import Preprocessor


if __name__ == "__main__":
    run_dir = "./run_dir"
    Utils.create_directories(run_dir=run_dir)

    # ? Changing the preprocessor_config values will change the preprocessing steps
    '''
    Default values are as follows
        "Normalizer": "MinMaxScaler",
        "Encoder": "OneHotEncoder",
        "excls_cols": ["CustomerID"],
        "categorical_cols": ['Gender'],
    '''
    Utils.preprocessor_config["Normalizer"] = "MinMaxScaler"
    Utils.preprocessor_config["Encoder"] = "LabelEncoder"
    dataset = Utils.load_data()

    # Plotting the dataset
    Monitor.run(dataset)

    preprocessor = Preprocessor(dataset)

    #! the final preprocessed dataset is returned with the following line
    dataset_preprocessed = preprocessor.preprocess()

    # print(dataset_preprocessed.head())
    print("main.py executed successfully")
