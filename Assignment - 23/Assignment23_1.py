#Assignment 23 - Problem 1 - Python Machine learning basics

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Dimension of data is : ", dataFrame.shape)

    print(line)

    print("Column names of dataframe are :\n", dataFrame.columns)

    print(line)

    print("Data type of dataframe are :\n", dataFrame.dtypes)

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


    # Q1: Create a DataFrame for student marks and print basic information like shape, columns, and
    # data types.
    # data = {
    # 'Name': ['Amit', 'Sagar', 'Pooja'],
    # 'Math': [85, 90, 78],
    # 'Science': [92, 88, 80],
    # 'English': [75, 85, 82]
    # }
    

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 23>python Assignment23_1.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Dimension of data is :  (3, 4)
    # ------------------------------------------------------------------------------------------------------------------------
    # Column names of dataframe are :
    # Index(['Name', 'Math', 'Science', 'English'], dtype='object')
    # ------------------------------------------------------------------------------------------------------------------------
    # Data type of dataframe are :
    # Name       object
    # Math        int64
    # Science     int64
    # English     int64
    # dtype: object
    # ------------------------------------------------------------------------------------------------------------------------

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 23>python Assignment23_1.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Dimension of data is :  (3, 4)
    # ------------------------------------------------------------------------------------------------------------------------
    # Column names of dataframe are :
    # Index(['Name', 'Math', 'Science', 'English'], dtype='object')
    # ------------------------------------------------------------------------------------------------------------------------
    # Data type of dataframe are :
    # Name       object
    # Math        int64
    # Science     int64
    # English     int64
    # dtype: object
    # ------------------------------------------------------------------------------------------------------------------------