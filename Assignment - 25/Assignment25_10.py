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

    X_Axis = dataFrame[["Age","Salary"]]
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
    data =  {
            'Age': [25, 30, 45, 35, 22],
            'Salary': [50000, 60000, 80000, 65000, 45000],
            'Purchased': [1, 0, 1, 0, 1]
            }
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q10: Split a DataFrame with multiple features into train-test for supervised learning.
    # data = {
    # 'Age': [25, 30, 45, 35, 22],
    # 'Salary': [50000, 60000, 80000, 65000, 45000],
    # 'Purchased': [1, 0, 1, 0, 1]
    # }

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_10.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Age  Salary  Purchased
    # 0   25   50000          1
    # 1   30   60000          0
    # 2   45   80000          1
    # 3   35   65000          0
    # 4   22   45000          1
    # ------------------------------------------------------------------------------------------------------------------------
    # X_train dataset of provided dataframe is :
    #     Age  Salary
    # 4   22   45000
    # 2   45   80000
    # 0   25   50000
    # 3   35   65000
    # ------------------------------------------------------------------------------------------------------------------------
    # X_test dataset of provided dataframe is :
    #     Age  Salary
    # 1   30   60000
    # ------------------------------------------------------------------------------------------------------------------------
    # Y_train dataset of provided dataframe is :
    #     Purchased
    # 4          1
    # 2          1
    # 0          1
    # 3          0
    # ------------------------------------------------------------------------------------------------------------------------
    # Y_test dataset of provided dataframe is :
    #     Purchased
    # 1          0
    # ------------------------------------------------------------------------------------------------------------------------