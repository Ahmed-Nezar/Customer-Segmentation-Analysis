from src.utils import Utils
from src.preprocessing import Preprocessor
# Any other imports you want to add can be added here

if __name__ == "__main__":
    run_dir = "./run_dir"
    Utils.create_directories(run_dir=run_dir)
    print("main.py executed successfully")
    # Any other code you want to run when the main.py file is executed

    Utils.preprocessor_config = {
        "Normalizer": "MinMaxScaler",
        "Encoder": "OneHotEncoder",
        "Imputer": "SimpleImputer",
        "Imputer_strategy": "mean",
    }

    preprocessor = Preprocessor()
    dataset_preprocessed = preprocessor.preprocess()
