#Assignment 24 - Problem 8 - Python Machine learning basics

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show


def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    figure()
    dataFrame["Math"].plot.hist().set_title("Math Marks")
    plt.savefig("MathHistogram.png")
    show()

    print("Histogram image is saved as MathHistogram.png")

    print(line)


    

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


    # Q8: Plot a histogram of math marks.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_8.py
    # ------------------------------------------------------------------------------------------------------------------------
    # Original data of dataframe is :
    #     Name  Math  Science  English
    # 0   Amit    85       92       75
    # 1  Sagar    90       88       85
    # 2  Pooja    78       80       82
    # ------------------------------------------------------------------------------------------------------------------------
    # Histogram image is saved as MathHistogram.png
    # ------------------------------------------------------------------------------------------------------------------------