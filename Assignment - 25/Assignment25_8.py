#Assignment 25 - Problem 8 - Python Machine learning basics

import numpy as np
import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)

    meanValues = dataFrame.mean()

    dataFrame = dataFrame.fillna(meanValues)

    print("Updated dataset : \n", dataFrame.head())

    print(line)

def main():
    data = {'Marks': [85, np.nan, 90, np.nan, 95]}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q8: Fill missing values in a numeric column using interpolation.
    # data = {'Marks': [85, np.nan, 90, np.nan, 95]}

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_8.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Marks
    # 0   85.0
    # 1    NaN
    # 2   90.0
    # 3    NaN
    # 4   95.0
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataset :
    #     Marks
    # 0   85.0
    # 1   90.0
    # 2   90.0
    # 3   90.0
    # 4   95.0
    # ------------------------------------------------------------------------------------------------------------------------