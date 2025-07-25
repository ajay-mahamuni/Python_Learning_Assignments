#Assignment 24 - Problem 9 - Python Machine learning basics

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show


def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataframe : \n", dataFrame.head())

    print(line)

    dataFrame = dataFrame.rename(columns={"Math" : "Mathematics"})

    print("Updated dataframe : \n", dataFrame.head())

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


    # Q9: Rename 'Math' column to 'Mathematics'.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_9.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataframe :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataframe :
    #     Name  Mathematics  Science  English
    # 0   Amit           85       92       75
    # 1  Sagar           90       88       85
    # 2  Pooja           78       80       82
    # ------------------------------------------------------------------------------------------------------------------------