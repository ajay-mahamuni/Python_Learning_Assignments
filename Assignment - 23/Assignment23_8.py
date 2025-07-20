#Assignment 23 - Problem 8 - Python Machine learning basics

import matplotlib.pyplot as plt

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    fiterData = dataFrame[dataFrame["Name"] == "Amit"]

    print("Filter Data :", fiterData)
    print(line)

    LineChart(fiterData)

def LineChart(dataFrame):
    
    X_Axis = dataFrame["Name"]
    subjects = ["Math","Science","English"]
    marks = dataFrame[subjects].values[0]

    
    plt.figure(figsize=(8,6))
    plt.plot(subjects,marks,color="red",label="Marks",linewidth=1.2,linestyle="--", marker="o")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Amit's Marks in each Subject")
    plt.legend()
    # plt.grid(True)
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


    # Q8: Plot a line chart of marks for 'Amit' across all subjects.a