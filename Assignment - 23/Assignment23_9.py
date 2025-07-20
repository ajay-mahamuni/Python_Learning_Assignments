#Assignment 23 - Problem 9 - Python Machine learning basics

import pandas as pd
import numpy as np

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original Dataset : \n", dataFrame.head())

    print(line)

    mean_values = dataFrame[["Math","Science","English"]].mean()

    print("Mean values : \n",mean_values)
    
    print(line)

    updatedDataFrame = dataFrame.fillna(mean_values)

    print("Updated Dataset : \n", updatedDataFrame.head())

    print(line)

    

def main():
    data = { 
                "Name" :    ["Amit", "Sagar", "Pooja"],
                "Math":     [np.nan,90,78],
                "Science":  [92,np.nan,80],
                "English":  [75,85,82]
            }       
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()


    # Q9: Create a DataFrame with missing values and fill them with column mean.
    # data2 = {
    # 'Name': ['Amit', 'Sagar', 'Pooja'],
    # 'Math': [np.nan, 76, 88],
    # 'Science': [91, np.nan, 85]
    # }

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 23>python Assignment23_9.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original Dataset :
    #     Name  Math  Science  English
    # 0   Amit   NaN     92.0       75
    # 1  Sagar  90.0      NaN       85
    # 2  Pooja  78.0     80.0       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Mean values :
    # Math       84.000000
    # Science    86.000000
    # English    80.666667
    # dtype: float64
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated Dataset :
    #     Name  Math  Science  English
    # 0   Amit  84.0     92.0       75
    # 1  Sagar  90.0     86.0       85
    # 2  Pooja  78.0     80.0       82
    # ------------------------------------------------------------------------------------------------------------------------