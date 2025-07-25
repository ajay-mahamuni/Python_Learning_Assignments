#Assignment 25 - Problem 6 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)    

    replacementMap = {
    "A+": "Excellent",
    "A" : "Very Good",
    "B+": "Good",
    "B" : "Average",
    "C" : "Poor"}

    dataFrame.replace(replacementMap,inplace=True)

    print("Updated dataset : \n", dataFrame.head())

    print(line)    



def main():
    data = {"Grade": ["A+", "B", "A", "C", "B+"]}
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q6: Replace multiple values in a column using a dictionary.
    # data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
    # Replace as
    # 'A+': ‘Excellent'
    # 'A': 'Very Good’
    # 'B+': ‘Good'
    # 'B': ‘Average'
    # 'C': 'Poor'

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 25>python Assignment25_6.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    # Grade
    # 0    A+
    # 1     B
    # 2     A
    # 3     C
    # 4    B+
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataset :
    #         Grade
    # 0  Excellent
    # 1    Average
    # 2  Very Good
    # 3       Poor
    # 4       Good
    # ------------------------------------------------------------------------------------------------------------------------