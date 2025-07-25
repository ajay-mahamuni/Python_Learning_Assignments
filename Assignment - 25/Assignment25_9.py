#Assignment 25 - Problem 9 - Python Machine learning basics

import numpy as np
import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)

    dataFrame["Status"] = np.where(dataFrame["Marks"] <= 50, "Fail", "Pass")

    print("Updated dataset : \n", dataFrame.head())

    print(line)

    

def main():
    data = {'Marks': [45, 67, 88, 32, 76]}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q9: Replace values in 'Marks' less than 50 with 'Fail' using where().
    # data = {'Marks': [45, 67, 88, 32, 76]}

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_9.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Marks
    # 0     45
    # 1     67
    # 2     88
    # 3     32
    # 4     76
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataset :
    #     Marks Status
    # 0     45   Fail
    # 1     67   Pass
    # 2     88   Pass
    # 3     32   Fail
    # 4     76   Pass
    # ------------------------------------------------------------------------------------------------------------------------