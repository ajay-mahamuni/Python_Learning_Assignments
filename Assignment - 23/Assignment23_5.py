#Assignment 23 - Problem 5 - Python Machine learning basics

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    dataFrame["Name"] = dataFrame["Name"].replace("Pooja", "Puja")

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


    # Q5: Replace 'Pooja' with 'Puja' in the 'Name' column.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 23>python Assignment23_5.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original data of dataframe is :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Modified data of dataframe is :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2   Puja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------