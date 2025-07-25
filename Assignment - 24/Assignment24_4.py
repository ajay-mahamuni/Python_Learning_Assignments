#Assignment 24 - Problem 4 - Python Machine learning basics

import matplotlib.pyplot as plt

import pandas as pd

def LoadDataFrame(data):

    line = "--"*60

    dataFrame = pd.DataFrame(data)

    print(line)

    print("Original data of dataframe is : \n", dataFrame.head())

    print(line)

    fiterData = dataFrame[dataFrame["Name"] == "Sagar"]

    print("Filter Data :\n", fiterData)
    print(line)

    LineChart(fiterData)

def LineChart(dataFrame):
    
    subjects = dataFrame.columns[[1,2,3]]
    marks = dataFrame[subjects].values[0]
    
    plt.figure(figsize=(8,6))
    plt.pie(marks,labels=subjects,autopct="%1.1f%%",startangle=90,shadow=True)

    
    plt.axis("equal")
    plt.title("Sagar's Marks in each Subject")
    plt.savefig("PieChart.png")
    plt.show()

    print("Pie chart of marks in each Subject saved as PieChart.png")
    

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


    # Q4: Plot a pie chart of subject marks for 'Sagar'.

    #    D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 24>python Assignment24_4.py
    #     ------------------------------------------------------------------------------------------------------------------------
    #     Original data of dataframe is :
    #         Name  Math  Science  English
    #     0   Amit    85       92       75
    #     1  Sagar    90       88       85
    #     2  Pooja    78       80       82
    #     ------------------------------------------------------------------------------------------------------------------------
    #     Filter Data :
    #         Name  Math  Science  English
    #     1  Sagar    90       88       85
    #     ------------------------------------------------------------------------------------------------------------------------
    #     Pie chart of marks in each Subject saved as PieChart.png