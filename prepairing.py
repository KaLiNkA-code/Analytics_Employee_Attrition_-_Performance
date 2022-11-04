import pandas as pd
from sklearn.model_selection import train_test_split


class Prepairing_data:
    """Class for prepairing anyone dataset"""

    def __init__(self, dataset: pd.DataFrame) -> None:
        self.dataset = dataset

    def data_split(self, target: str = "HourlyRate", count: int = 3) -> tuple:
        """returned tuple with: train_target, train_X, val_target, val_X, test_target, test_X"""
        train_df, val_test_df = train_test_split(self.dataset, train_size=0.6, random_state=0)
        val_df, test_df = train_test_split(val_test_df, test_size=0.5, random_state=0)

        train_target = test_df[target]
        train_X = pd.DataFrame()
        _index = 0
        for i in train_df.columns:
            train_X.insert(_index, i, train_df[[i]])
            _index += 1

        # val_target = val_df[target]
        # val_X = pd.DataFrame()
        # _index = 0
        # for i in val_df.columns:
        #     val_X.insert(_index, i, train_df[[i]])
        #     _index += 1

        # test_target = test_df[target]
        # test_X = pd.DataFrame()
        # _index = 0
        # for i in test_df.columns:
        #     test_X.insert(_index, i, train_df[[i]])
        #     _index += 1

        return (train_target, train_X)  # val_target, val_X, test_target, test_X)

    def prepairing(mode: str = None) -> pd.DataFrame:
        """Mode: normalize: norm || standart_scaller: st_s"""
        if mode:
            if mode == "norm":
                pass
            elif mode == "st_s":
                pass
            else:
                pass
        else:
            pass

    def __str__(self) -> str:
        return self.dataset
