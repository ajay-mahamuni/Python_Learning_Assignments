#Assignment 24 - Problem 3 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)

    dataFrame["Total"] = dataFrame["Math"] + dataFrame["Science"] + dataFrame["English"]
    
    dataFrame["Gender"] = ["Male","Male","Female"]

    print("Updated dataset : \n", dataFrame.head())

    print(line)

    group_data = dataFrame.groupby("Gender")["Total"].mean()

    print("Group dataset with average of Total marks : \n", group_data.head())

    print(line)

def main():
    data = { 
                "Name" :    ["Amit", "Sagar", "Pooja"],
                "Math":     [85,90,78],
                "Science":  [92,88,80],
                "English":      [75,85,82]
            }       
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q3: Group students by gender and calculate average marks.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_3.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataset :
    #     Name  Math  Science  English  Total  Gender
    # 0   Amit    85       92       75    252    Male
    # 1  Sagar    90       88       85    263    Male
    # 2  Pooja    78       80       82    240  Female
    # ------------------------------------------------------------------------------------------------------------------------
    # Group dataset with average of Total marks :
    # Gender
    # Female    240.0
    # Male      257.5
    # Name: Total, dtype: float64
    # ------------------------------------------------------------------------------------------------------------------------