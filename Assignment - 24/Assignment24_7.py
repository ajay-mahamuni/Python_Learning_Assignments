#Assignment 24 - Problem 7 - Python Machine learning basics

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    dataFrame["Total"] = dataFrame["Math"] + dataFrame["Science"] + dataFrame["English"]

    print("Total added to dataframe : \n", dataFrame.head())

    print(line)

    dataFrame["Status"] = np.where(dataFrame["Total"] >= 250, "Pass", "Fail")

    print("Modified data in dataframe : \n", dataFrame.head())

    print(line)

    dataFrame.to_csv("Result.csv",index=False)

    print("DataFrame successfully exported to Result.csv")

    print(line)

    
def main():
    data = { 
                "Name" :    ["Amit", "Sagar", "Pooja"],
                "Math":     [85,90,78],
                "Science":  [92,88,80],
                "English":  [75,85,82]
            }       
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()


    # Q7: Export the final DataFrame to a CSV file.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_7.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original data of dataframe is :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Total added to dataframe :
    #     Name  Math  Science  English  Total
    # 0   Amit    85       92       75    252
    # 1  Sagar    90       88       85    263
    # 2  Pooja    78       80       82    240
    # ------------------------------------------------------------------------------------------------------------------------
    # Modified data in dataframe :
    #     Name  Math  Science  English  Total Status
    # 0   Amit    85       92       75    252   Pass
    # 1  Sagar    90       88       85    263   Pass
    # 2  Pooja    78       80       82    240   Fail
    # ------------------------------------------------------------------------------------------------------------------------
    # DataFrame successfully exported to Result.csv
    # ------------------------------------------------------------------------------------------------------------------------