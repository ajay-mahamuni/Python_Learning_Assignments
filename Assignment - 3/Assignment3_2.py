#Assignment 3 - Problem 2 - Maximum number from  list

from functools import reduce

maxNum = lambda num1,num2 : num1 if num1 > num2 else num2


# def maxNumber(num1,num2):    
#     if(num1 > num2):
#         return num1
#     else:
#         return num2  

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
        
        rData = reduce(maxNum,dataList)

        print("Maximum numbers from list is : ", rData)

if __name__ == "__main__":
    main()


    #   2.Write a program which accept N numbers from user and store it into List. Return Maximum
    # number from that List.
    # Input : Number of elements : 7
    # Input Elements : 13 5 45 7 4 56 34
    # Output : 56


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 3>python Assignment3_2.py
    # Enter number of elements : 5
    # 45
    # 12
    # 65
    # 78
    # 45
    # Maximum numbers from list is :  78