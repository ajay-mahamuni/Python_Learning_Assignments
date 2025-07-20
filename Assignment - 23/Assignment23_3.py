#Assignment 23 - Problem 3 - Python Machine learning basics

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    dataFrame["Total"] = dataFrame["Math"] + dataFrame["Science"] + dataFrame["English"]

    print("Modified data of dataframe is : \n", dataFrame.head())

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


    # Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 23>python Assignment23_3.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original data of dataframe is :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Modified data of dataframe is :
    #     Name  Math  Science  English  Total
    # 0   Amit    85       92       75    252
    # 1  Sagar    90       88       85    263
    # 2  Pooja    78       80       82    240
    # ------------------------------------------------------------------------------------------------------------------------