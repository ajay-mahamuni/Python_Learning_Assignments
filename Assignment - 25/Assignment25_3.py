#Assignment 25 - Problem 3 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)    

    label_Encoder = LabelEncoder()

    dataFrame["City_Encoded"] = label_Encoder.fit_transform(dataFrame["City"])

    print("Encoded dataframe : \n", dataFrame.head())

    print(line)   
    

def main():
    data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q3: Apply Label Encoding to a 'City' column.
    # data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_3.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     City
    # 0    Pune
    # 1  Mumbai
    # 2   Delhi
    # 3    Pune
    # 4   Delhi
    # ------------------------------------------------------------------------------------------------------------------------
    # Encoded dataframe :
    #     City  City_Encoded
    # 0    Pune             2
    # 1  Mumbai             1
    # 2   Delhi             0
    # 3    Pune             2
    # 4   Delhi             0
    # ------------------------------------------------------------------------------------------------------------------------