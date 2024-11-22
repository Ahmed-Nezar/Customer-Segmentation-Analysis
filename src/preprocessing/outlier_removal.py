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

    def remove_outliers_IQR(self):
        """
        Removes outliers detected by the IQR method.
        Equivalent to the standalone `outliers_removal_IQR` function.
        """
        # Detect outliers using IQR
        self.detect_outliers_IQR()
        
        # Find all columns starting with "OUTLIER"
        outliers_columns = [col for col in self.dataset.columns if col.startswith("OUTLIER")]
        
        # Filter out rows with any IQR-based outliers
        outlier_cols = [col for col in self.dataset.columns if col.startswith("OUTLIER_IQR")]
        self.dataset = self.dataset[~self.dataset[outlier_cols].any(axis=1)]
        
        # Drop all "OUTLIER" columns and the 'CustomerID' column
        self.dataset.drop(columns=outliers_columns, inplace=True, errors='ignore')
        self.dataset.drop(columns=['CustomerID'], inplace=True, errors='ignore')
        
        return self.dataset


    def remove_outliers_zscore(self, zscore_threshold=3):
        """
        Removes outliers detected by the Z-score method.
        Equivalent to the standalone `outliers_removal_zscore` function.

        Parameters:
            zscore_threshold (float): The Z-score threshold to flag outliers.
        """
        # Detect outliers using Z-score
        self.detect_outliers_zscore(threshold=zscore_threshold)
        
        # Find all columns starting with "OUTLIER"
        outliers_columns = [col for col in self.dataset.columns if col.startswith("OUTLIER")]
        
        # Filter out rows with any Z-score-based outliers
        outlier_cols = [col for col in self.dataset.columns if col.startswith("OUTLIER_ZSCORE")]
        self.dataset = self.dataset[~self.dataset[outlier_cols].any(axis=1)]
        
        # Drop all "OUTLIER" columns and the 'CustomerID' column
        self.dataset.drop(columns=outliers_columns, inplace=True, errors='ignore')
        self.dataset.drop(columns=['CustomerID'], inplace=True, errors='ignore')
        
        return self.dataset

