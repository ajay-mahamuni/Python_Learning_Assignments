#Assignment 24 - Problem 10 - Python Machine learning basics

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    plt.boxplot(x=dataFrame["English"])

    plt.title("BoxPlot for English subject to check distribution and outliers")

    plt.ylabel("English Marks")

    plt.grid(True, axis="y")

    plt.savefig("BoxPlot-English.png")

    plt.show()


    

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


    # Q10: Plot a boxplot for English marks to check distribution and outliers.