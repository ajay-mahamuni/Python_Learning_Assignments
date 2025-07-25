#Assignment 24 - Problem 6 - Python Machine learning basics

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

    passCount = len(dataFrame[dataFrame["Status"] == "Pass"])
    failCount = len(dataFrame[dataFrame["Status"] == "Fail"])

    print("Pass student count : ", passCount, "\n") 
    print("Fail student count : ", failCount, "\n")

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


    # Q6: Count how many students passed.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_6.py
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
    # Pass student count :  2

    # Fail student count :  1

    # ------------------------------------------------------------------------------------------------------------------------