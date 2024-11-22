import pandas as pd
import numpy as np
from scipy.stats import zscore


class OutlierRemoval:
    def __init__(self, dataset):
        """
        Initializes the OutlierRemoval class.

        Parameters:
            dataset (pd.DataFrame): The dataset to process for outlier removal.
        """
        self.dataset = dataset.copy()

    def detect_outliers_IQR(self):
        """
        Detects outliers in numerical columns using the IQR method.
        Adds new columns indicating outliers for each numerical column.
        """
        for col in self.dataset.select_dtypes(include=np.number).columns:
            Q1 = self.dataset[col].quantile(0.25)
            Q3 = self.dataset[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            self.dataset[f'OUTLIER_IQR_{col}'] = (
                (self.dataset[col] < lower_bound) | (self.dataset[col] > upper_bound)
            )
        return self.dataset

    def detect_outliers_zscore(self, threshold=3):
        """
        Detects outliers in numerical columns using the Z-score method.
        Adds new columns indicating outliers for each numerical column.

        Parameters:
            threshold (float): The Z-score threshold to flag outliers.
        """
        numerical_data = self.dataset.select_dtypes(include=np.number)
        z_scores = pd.DataFrame(zscore(numerical_data), columns=numerical_data.columns, index=self.dataset.index)

        for col in z_scores.columns:
            self.dataset[f'OUTLIER_ZSCORE_{col}'] = (np.abs(z_scores[col]) > threshold)

        return self.dataset

