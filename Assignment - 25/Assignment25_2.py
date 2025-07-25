#Assignment 25 - Problem 2 - Python Machine learning basics

import numpy as nm
import pandas as pd


def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)
    
    print("Current datatypes : \n", dataFrame.dtypes)

    print(line)

    dataFrame["Age"] = dataFrame["Age"].astype(int)

    print("Updated datatypes : \n", dataFrame.dtypes)

    print(line)

    print("Updated dataset : \n", dataFrame.head())

    print(line)


def main():
    data = {"Name": ['A', 'B', 'C'], "Age": [21.0, 22.0, 23.0]}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q2: Detect column data types and convert 'Age' from float to int.
    # data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_2.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    # Name   Age
    # 0    A  21.0
    # 1    B  22.0
    # 2    C  23.0
    # ------------------------------------------------------------------------------------------------------------------------
    # Current datatypes :
    # Name     object
    # Age     float64
    # dtype: object
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated datatypes :
    # Name    object
    # Age      int64
    # dtype: object
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataset :
    # Name  Age
    # 0    A   21
    # 1    B   22
    # 2    C   23
    # ------------------------------------------------------------------------------------------------------------------------