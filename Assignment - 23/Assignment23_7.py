#Assignment 23 - Problem 7 - Python Machine learning basics

import matplotlib.pyplot as plt

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    dataFrame["Total"] = dataFrame["Math"] + dataFrame["Science"] + dataFrame["English"]

    print("Modified data of dataframe is : \n", dataFrame.head())

    print(line)

    BarPlot(dataFrame)

def BarPlot(dataFrame):
    names = dataFrame["Name"]
    totalMarks = dataFrame["Total"]


    plt.figure(figsize=(8,6))
    plt.bar(names,totalMarks)
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Bar Plot of Total Marks for each Student")
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


    # Q7: Create a bar plot of student names vs total marks.