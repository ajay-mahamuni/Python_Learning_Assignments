#Assignment 23 - Problem 4 - Python Machine learning basics

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    filterDataFrame = dataFrame[dataFrame["Science"] > 85]

    print("Filtered data of dataframe is : \n", filterDataFrame.head())

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


    # Q4: Display students who scored more than 85 in Science.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 23>python Assignment23_4.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original data of dataframe is :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Filtered data of dataframe is :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # ------------------------------------------------------------------------------------------------------------------------