#Assignment 3 - Problem 3 - Minumum number from  list

from functools import reduce

minNum = lambda num1,num2 : num1 if num1 < num2 else num2

def main():
    size = int(input("Enter number of elements : "))

    dataList = []
    num = 0

    if size > 0:
        for i in range(size):

            num = input()

            if num.isdigit():
                dataList.append(int(num))
            else:
                print("Enter valid number")    
        
        rData = reduce(minNum,dataList)

        print("Maximum numbers from list is : ", rData)

if __name__ == "__main__":
    main()


    # 3.Write a program which accept N numbers from user and store it into List. Return Minimum
    # number from that List.
    # Input : Number of elements : 4
    # Input Elements : 13 5 45 7
    # Output : 5

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 3>python Assignment3_3.py
    # Enter number of elements : 5
    # 54
    # 32
    # 44
    # 98
    # 45
    # Maximum numbers from list is :  32