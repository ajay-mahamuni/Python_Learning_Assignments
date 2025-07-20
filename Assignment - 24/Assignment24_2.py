#Assignment 24 - Problem 2 - Python Machine learning basics

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)

    dataFrame["Gender"] = ["Male","Male","Female"]

    print("Updated dataset : \n", dataFrame.head())

    print(line)
    
    encoded_data = pd.get_dummies(dataFrame,columns=["Gender"],drop_first=False)

    print("Encoded dataset : \n", encoded_data)

    print(line)

    # encoder = OneHotEncoder(sparse_output=False)

    # onehot_encoded = encoder.fit_transform(dataFrame["Gender"])

    # onehot_dataframe = pd.DataFrame(onehot_encoded,columns=encoder.get_feature_names_out("Gender"))

    # print("One hot encoded dataset : \n", onehot_dataframe)

    # print(line)
    

    

def main():
    data = { 
                "Name" :    ["Amit", "Sagar", "Pooja"],
                "Math":     [85,90,78],
                "Science":  [92,88,80],
                "English":  [75,85,82]
            }       
    
    LoadDataFrame(data)
            

if __name__ == "__main__":
    main()

    # Q2: Create a gender column and perform one-hot encoding.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_2.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataset :
    #     Name  Math  Science  English  Gender
    # 0   Amit    85       92       75    Male
    # 1  Sagar    90       88       85    Male
    # 2  Pooja    78       80       82  Female
    # ------------------------------------------------------------------------------------------------------------------------
    # Encoded dataset :
    #     Name  Math  Science  English  Gender_Female  Gender_Male
    # 0   Amit    85       92       75          False         True
    # 1  Sagar    90       88       85          False         True
    # 2  Pooja    78       80       82           True        False
    # ------------------------------------------------------------------------------------------------------------------------