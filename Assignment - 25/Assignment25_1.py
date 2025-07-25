#Assignment 25 - Problem 1 - Python Machine learning basics

import numpy as nm
import pandas as pd


def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head)

    print(line)

    Q1 = dataFrame["Salary"].quantile(0.25)
    Q3 = dataFrame["Salary"].quantile(0.75)

    IQR = Q3 - Q1

    lowerBound = Q1 - 1.5 * IQR
    upperBound = Q3 + 1.5 * IQR

    outliers = dataFrame[(dataFrame["Salary"] < lowerBound) | (dataFrame["Salary"] > upperBound)]

    print("Outliers identified using IQR method : \n",outliers)

    print(line)
    

def main():
    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q1: Detect outliers in the 'Salary' column using the IQR method.
    # data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_1.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    # <bound method NDFrame.head of    Salary
    # 0   25000
    # 1   27000
    # 2   29000
    # 3   31000
    # 4   50000
    # 5  100000>
    # ------------------------------------------------------------------------------------------------------------------------
    # Outliers identified using IQR method :
    #     Salary
    # 5  100000
    # ------------------------------------------------------------------------------------------------------------------------