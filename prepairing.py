import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


class Prepairing_data:
    """Class for prepairing anyone dataset"""

    def __init__(self, dataset: pd.DataFrame) -> None:
        self.dataset = dataset
        self._train_X = pd.DataFrame
        self._train_target = pd.DataFrame
        self._val_target = pd.DataFrame
        self._val_X = pd.DataFrame
        self._test_target = pd.DataFrame
        self._test_X = pd.DataFrame

    def data_split(self, df, target: str = "HourlyRate", count: int = 3) -> tuple:
        """returned tuple with: train_target, train_X, val_target, val_X, test_target, test_X"""
        if count == 3:
            train_df, val_test_df = train_test_split(df, train_size=0.6, random_state=0)
            val_df, test_df = train_test_split(val_test_df, test_size=0.5, random_state=0)

            train_target = train_df[target]
            train_X = pd.DataFrame(train_df.drop(columns=[target], axis=1))

            val_target = val_df[target]
            val_X = pd.DataFrame(val_df.drop(columns=[target], axis=1))

            test_target = test_df[target]
            test_X = pd.DataFrame(test_df.drop(columns=[target], axis=1))

            self._train_X = train_X
            self._train_target = train_target
            self._val_target = val_target
            self._val_X = val_X
            self._test_target = test_target
            self._test_X = test_X

            return train_X, train_target, val_target, val_X, test_target, test_X

    def prepairing(self, mode: str = None) -> pd.DataFrame:
        """Mode: normalize: norm || standart_scaller: st_s"""
        columns = self.dataset.columns

        scaler = MinMaxScaler(feature_range=(-1, 1))
        scaler.fit(self.dataset)
        if mode:
            if mode == "norm":
                pass
            elif mode == "minmax":
                pass
            else:
                pass
        else:
            return pd.DataFrame(scaler.transform(self.dataset), columns=columns)

        # scaler = MinMaxScaler(feature_range=(0, 1))
        # # Fit on the training data
        # scaler.fit(X)
        # # Transform both the training and testing data
        # X = scaler.transform(X)
        # X_test = scaler.transform(X_test)

    def first_prepairing(self) -> pd.DataFrame:
        self.dataset.loc[(self.dataset["BusinessTravel"] == "Travel_Rarely"), ("BusinessTravel")] = 1
        self.dataset.loc[(self.dataset["BusinessTravel"] == "Travel_Frequently"), ("BusinessTravel")] = 2
        self.dataset.loc[(self.dataset["BusinessTravel"] == "Non-Travel"), ("BusinessTravel")] = 3

        self.dataset.loc[(self.dataset["Department"] == "Sales"), ("Department")] = 1
        self.dataset.loc[(self.dataset["Department"] == "Research & Development"), ("Department")] = 2
        self.dataset.loc[(self.dataset["Department"] == "Human Resources"), ("Department")] = 3

        self.dataset.loc[(self.dataset["EducationField"] == "Life Sciences"), ("EducationField")] = 1
        self.dataset.loc[(self.dataset["EducationField"] == "Other"), ("EducationField")] = 2
        self.dataset.loc[(self.dataset["EducationField"] == "Medical"), ("EducationField")] = 3
        self.dataset.loc[(self.dataset["EducationField"] == "Marketing"), ("EducationField")] = 4
        self.dataset.loc[(self.dataset["EducationField"] == "Technical Degree"), ("EducationField")] = 5
        self.dataset.loc[(self.dataset["EducationField"] == "Human Resources"), ("EducationField")] = 6

        self.dataset.loc[(self.dataset["Gender"] == "Male"), ("Gender")] = 0
        self.dataset.loc[(self.dataset["Gender"] == "Female"), ("Gender")] = 1

        self.dataset.loc[(self.dataset["JobRole"] == "Human Resources"), ("JobRole")] = 1
        self.dataset.loc[(self.dataset["JobRole"] == "Research Scientist"), ("JobRole")] = 2
        self.dataset.loc[(self.dataset["JobRole"] == "Laboratory Technician"), ("JobRole")] = 3
        self.dataset.loc[(self.dataset["JobRole"] == "Manufacturing Director"), ("JobRole")] = 4
        self.dataset.loc[(self.dataset["JobRole"] == "Healthcare Representative"), ("JobRole")] = 5
        self.dataset.loc[(self.dataset["JobRole"] == "Manager"), ("JobRole")] = 6
        self.dataset.loc[(self.dataset["JobRole"] == "Sales Representative"), ("JobRole")] = 7
        self.dataset.loc[(self.dataset["JobRole"] == "Research Director"), ("JobRole")] = 8
        self.dataset.loc[(self.dataset["JobRole"] == "Sales Executive"), ("JobRole")] = 9

        self.dataset.loc[(self.dataset["MaritalStatus"] == "Single"), ("MaritalStatus")] = 1
        self.dataset.loc[(self.dataset["MaritalStatus"] == "Married"), ("MaritalStatus")] = 2
        self.dataset.loc[(self.dataset["MaritalStatus"] == "Divorced"), ("MaritalStatus")] = 3

        self.dataset.loc[(self.dataset["OverTime"] == "No"), ("OverTime")] = 0
        self.dataset.loc[(self.dataset["OverTime"] == "Yes"), ("OverTime")] = 1

        return self.dataset

    def __str__(self) -> str:
        return self.dataset
