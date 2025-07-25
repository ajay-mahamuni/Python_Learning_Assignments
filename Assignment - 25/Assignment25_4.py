#Assignment 25 - Problem 4 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)    

    One_HotEncoding = OneHotEncoder(sparse_output=False)

    encodedColumn = One_HotEncoding.fit_transform(dataFrame[["Department"]])

    encodedDataFrame = pd.DataFrame(encodedColumn,columns=One_HotEncoding.get_feature_names_out(["Department"]))

    print("One-Hot Encoded dataframe : \n", encodedDataFrame.head())

    print(line)   

    

def main():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q4: Apply One-Hot Encoding to a 'Department' column.
    # data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_4.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    # Department
    # 0         HR
    # 1         IT
    # 2    Finance
    # 3         HR
    # 4         IT
    # ------------------------------------------------------------------------------------------------------------------------
    # One-Hot Encoded dataframe :
    #     Department_Finance  Department_HR  Department_IT
    # 0                 0.0            1.0            0.0
    # 1                 0.0            0.0            1.0
    # 2                 1.0            0.0            0.0
    # 3                 0.0            1.0            0.0
    # 4                 0.0            0.0            1.0
    # ------------------------------------------------------------------------------------------------------------------------