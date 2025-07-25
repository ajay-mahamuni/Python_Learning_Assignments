#Assignment 25 - Problem 5 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)    

    X_Axis = dataFrame[["Age"]]
    Y_Axis = dataFrame[["Purchased"]]
    
    X_train, X_test, Y_train, Y_test = train_test_split(X_Axis,Y_Axis,test_size=0.2,random_state=42)

    print("X_train dataset of provided dataframe is : \n",X_train)
    print(line)
    print("X_test dataset of provided dataframe is : \n",X_test)
    print(line)
    print("Y_train dataset of provided dataframe is : \n",Y_train)
    print(line)
    print("Y_test dataset of provided dataframe is : \n",Y_test)
    print(line)    

def main():
    data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q5: Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets.
    # data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}

    
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_5.py
    #     ------------------------------------------------------------------------------------------------------------------------
    #     Original dataset :
    #         Age  Purchased
    #     0   22          0
    #     1   25          1
    #     2   47          1
    #     3   52          0
    #     4   46          1
    #     ------------------------------------------------------------------------------------------------------------------------
    #     X_train dataset of provided dataframe is :
    #         Age
    #     5   56
    #     2   47
    #     4   46
    #     3   52
    #     ------------------------------------------------------------------------------------------------------------------------
    #     X_test dataset of provided dataframe is :
    #         Age
    #     0   22
    #     1   25
    #     ------------------------------------------------------------------------------------------------------------------------
    #     Y_train dataset of provided dataframe is :
    #         Purchased
    #     5          0
    #     2          1
    #     4          1
    #     3          0
    #     ------------------------------------------------------------------------------------------------------------------------
    #     Y_test dataset of provided dataframe is :
    #         Purchased
    #     0          0
    #     1          1
    #     ------------------------------------------------------------------------------------------------------------------------