import sys

import pandas as pd
from pandas import DataFrame
from io import StringIO
import numpy as np

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split


def data_generation(seed: int = 77,
                    train_indices_dir: str = 'train_indices.npy',
                    test_indices_dir: str = 'test_indices.npy',
                    test_size: float = 0.3,
                    ):
    """
    Function to generate a credit risk train/test data split from
    http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data
    and store a train/test data split in the form of an index array

    Args:
        seed: Random seed.
        train_indices_dir: Directory to file where training index array should be stored.
        test_indices_dir: Directory to file where test index array should be stored.
        test_size: Fraction of all data which is to be used for the test data.
    """

    if sys.version_info[0] == 3:
        from urllib.request import urlopen
    else:
        from urllib import urlopen
    with urlopen("http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/"
                 "german/german.data") as url:
        byte_data = url.read()

    str_data = StringIO(str(byte_data, 'utf-8'))
    # Load data headers
    columns = ['Existing_CheckingAccount_Status',
            'Duration_In_Month',
              'Credit_History',
              'Loan_Purpose',
              'Credit_Amount',
              'Saving_Account_Or_Bonds',
              'Present_Employment_Since',
              'Installment_Rate_Pct_Disposable_Income',
              'Marital_Status_And_Gender',
              'Other_Debtors_Or_Guarantors',
              'Current_Residence_Duration',
              'Property',
              'Age_In_Years',
              'Other_Installment_Plans',
              'Housing_Status',
              'Number_Existing_Credits_At_Bank',
              'Employment_Status',
              'Number_People_Liable_Maintenance',
              'Telephone_Registration_Status',
              'Foreign_Worker',
              'Credit_Risk_Status']
    # Load data frame
    df = pd.read_csv(str_data,
                     sep=" ",
                     header=None,
                     names=columns,
                     dtype={'Existing_CheckingAccount_Status': str,
                             'Duration_In_Month': int,
                             'Credit_History': str,
                             'Loan_Purpose': str,
                             'Credit_Amount': int,
                             'Saving_Account_Or_Bonds': str,
                             'Present_Employment_Since': str,
                             'Installment_Rate_Pct_Disposable_Income': int,
                             'Marital_Status_And_Gender': str,
                             'Other_Debtors_Or_Guarantors': str,
                             'Current_Residence_Duration': int,
                             'Property': str,
                             'Age_In_Years': int,
                             'Other_Installment_Plans': str,
                             'Housing_Status': str,
                             'Number_Existing_Credits_At_Bank': int,
                             'Employment_Status': str,
                             'Number_People_Liable_Maintenance': int,
                             'Telephone_Registration_Status': str,
                             'Foreign_Worker': str,
                             'Credit_Risk_Status': str})
    X, y = df.drop('Credit_Risk_Status', axis=1), pd.DataFrame(LabelEncoder().fit_transform(df['Credit_Risk_Status']),
                    columns=["is_credit_risky"])
    categorical_X = pd.get_dummies(X.select_dtypes('object'))
    numerical_X = pd.DataFrame(StandardScaler().fit_transform(X.select_dtypes('int')),
                               columns=["Duration_In_Month_zscl",
                                        "Credit_Amount_zscl",
                                        "Installment_Rate_Pct_Disposable_Income_zscl",
                                        "Current_Residence_Duration_zscl",
                                        "Age_In_Years_zscl",
                                        "Number_Existing_Credits_At_Bank_zscl",
                                        "Number_People_Liable_Maintenance_zscl"])
    concatenated_X = pd.concat([categorical_X, numerical_X], axis=1)
    # Concatenate labels and data
    X_Y = pd.concat([concatenated_X, y], axis=1)
    # Generate train/test split
    train, test = train_test_split(X_Y, test_size=test_size, stratify=X_Y['is_credit_risky'],
                                   random_state=seed)
    # Load indices which refer to train respectively test data
    np.save(train_indices_dir, np.array(train.index))
    np.save(test_indices_dir, np.array(test.index))
    return


def data_loading(train_indices_dir: str = 'train_indices.npy',
                 test_indices_dir: str = 'test_indices.npy') -> DataFrame:
    """
    Function to load a pre-generated credit risk train/test data split--see test_indices.npy and train_indices.npy--
    from http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data and
    returns the train respectively test data as a pandas DataFrame

    Args:
        train_indices_dir: Directory to file where training index array is stored.
        test_indices_dir: Directory to file where test index array is stored.
    """
    if sys.version_info[0] == 3:
        from urllib.request import urlopen
    else:
        from urllib import urlopen
    with urlopen("http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/"
                 "german/german.data") as url:
        byte_data = url.read()

    str_data = StringIO(str(byte_data, 'utf-8'))
    # Load data headers
    columns = ['Existing_CheckingAccount_Status',
              'Duration_In_Month',
              'Credit_History',
              'Loan_Purpose',
              'Credit_Amount',
              'Saving_Account_Or_Bonds',
              'Present_Employment_Since',
              'Installment_Rate_Pct_Disposable_Income',
              'Marital_Status_And_Gender',
              'Other_Debtors_Or_Guarantors',
              'Current_Residence_Duration',
              'Property',
              'Age_In_Years',
              'Other_Installment_Plans',
              'Housing_Status',
              'Number_Existing_Credits_At_Bank',
              'Employment_Status',
              'Number_People_Liable_Maintenance',
              'Telephone_Registration_Status',
              'Foreign_Worker',
              'Credit_Risk_Status']
    # Load data frame
    df = pd.read_csv(str_data,
                     sep=" ",
                     header=None,
                     names=columns,
                     dtype={'Existing_CheckingAccount_Status': str,
                             'Duration_In_Month': int,
                             'Credit_History': str,
                             'Loan_Purpose': str,
                             'Credit_Amount': int,
                             'Saving_Account_Or_Bonds': str,
                             'Present_Employment_Since': str,
                             'Installment_Rate_Pct_Disposable_Income': int,
                             'Marital_Status_And_Gender': str,
                             'Other_Debtors_Or_Guarantors': str,
                             'Current_Residence_Duration': int,
                             'Property': str,
                             'Age_In_Years': int,
                             'Other_Installment_Plans': str,
                             'Housing_Status': str,
                             'Number_Existing_Credits_At_Bank': int,
                             'Employment_Status': str,
                             'Number_People_Liable_Maintenance': int,
                             'Telephone_Registration_Status': str,
                             'Foreign_Worker': str,
                             'Credit_Risk_Status': str})
    X, y = df.drop('Credit_Risk_Status', axis=1), pd.DataFrame(LabelEncoder().fit_transform(df['Credit_Risk_Status']),
                    columns=["is_credit_risky"])
    categorical_X = pd.get_dummies(X.select_dtypes('object'))
    numerical_X = pd.DataFrame(StandardScaler().fit_transform(X.select_dtypes('int')),
                               columns=["Duration_In_Month_zscl",
                                        "Credit_Amount_zscl",
                                        "Installment_Rate_Pct_Disposable_Income_zscl",
                                        "Current_Residence_Duration_zscl",
                                        "Age_In_Years_zscl",
                                        "Number_Existing_Credits_At_Bank_zscl",
                                        "Number_People_Liable_Maintenance_zscl"])
    concatenated_X = pd.concat([categorical_X, numerical_X], axis=1)
    # Concatenate labels and data
    X_Y = pd.concat([concatenated_X, y], axis=1)
    # Load indices which refer to train respectively test data
    train_indices = np.load(train_indices_dir)
    test_indices = np.load(test_indices_dir)
    # Generate train respectively test data from indices
    train = X_Y.iloc[train_indices]
    test = X_Y.iloc[test_indices]
    return train, test