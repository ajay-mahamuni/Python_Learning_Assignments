#Assignment 3 - Problem 1 - Sum of numbers in list

from functools import reduce

sum = lambda num1, num2 : num1 + num2

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
        
        rData = reduce(sum,dataList)

        print("Sum of input numbers is : ", rData)

if __name__ == "__main__":
    main()


    #1.Write a program which accept N numbers from user and store it into List. Return addition of all
    # elements from that List.
    # Input : Number of elements : 6
    # Input Elements : 13 5 45 7 4 56
    # Output : 130

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 3>python Assignment3_1.py
    # Enter number of elements : 4
    # 10
    # 20
    # 30
    # 40
    # Sum of input numbers is :  100