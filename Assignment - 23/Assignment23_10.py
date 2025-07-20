#Assignment 23 - Problem 10 - Python Machine learning basics

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original dataset : \n", dataFrame.head())

    print(line)

    dataFrame = dataFrame.drop("English",axis=1)

    print("Updated dataset : \n", dataFrame.head())

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


    # Q10: Drop the 'English' column from original DataFrame.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 23>python Assignment23_10.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original dataset :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Updated dataset :
    #     Name  Math  Science
    # 0   Amit    85       92
    # 1  Sagar    90       88
    # 2  Pooja    78       80
    # ------------------------------------------------------------------------------------------------------------------------