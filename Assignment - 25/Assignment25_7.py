#Assignment 25 - Problem 7 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)    

    scaler = MinMaxScaler()

    scaledData = scaler.fit_transform(dataFrame)

    print("Normalized dataframe : \n", scaledData)

    print(line)


def main():
    data = {'Age': [18, 22, 25, 30, 35]}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q7: Normalize 'Age' column using Min-Max Scaling.
    # data = {'Age': [18, 22, 25, 30, 35]}

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_7.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Age
    # 0   18
    # 1   22
    # 2   25
    # 3   30
    # 4   35
    # ------------------------------------------------------------------------------------------------------------------------
    # Normalized dataframe :
    # [[0.        ]
    # [0.23529412]
    # [0.41176471]
    # [0.70588235]
    # [1.        ]]
    # ------------------------------------------------------------------------------------------------------------------------