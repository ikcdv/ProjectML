
import pandas as pd
import os


def data_load():
    """Load csv files to DataFrame"""

    df_train = pd.read_csv(os.path.join('data', 'train_data.csv'), header=None)
    df_test = pd.read_csv(os.path.join('data', 'test_data.csv'), header=None)
    df_train_labels = pd.read_csv(os.path.join(
        'data', 'train_labels.csv'), header=None)

    return [df_train, df_test, df_train_labels]
