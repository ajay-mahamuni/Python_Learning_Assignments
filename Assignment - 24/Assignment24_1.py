#Assignment 24 - Problem 1 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)

    scaler = MinMaxScaler()

    scaledData = scaler.fit_transform(dataFrame[["Math"]])

    print("Normalized data of Maths : \n", scaledData)

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

    # Q1: Normalize the 'Math' scores using Min-Max scaling.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_1.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Normalized data of Maths :
    # [[0.58333333]
    # [1.        ]
    # [0.        ]]
    # ------------------------------------------------------------------------------------------------------------------------