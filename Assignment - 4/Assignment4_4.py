#Assignment 4 - Problem 4 - Filter map reduce to calculate square of even numbers from list

from functools import reduce

NumberFilter = lambda num1 : num1 % 2 == 0

NumberMap = lambda num1 : num1**2

NumberReduce = lambda num1, num2 : num1 + num2

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

        print("Input List : ", dataList)

        #lambda function to filter numbers which are even
        fData = list(filter(NumberFilter,dataList))

        print("List after filter : ",fData)

        #lambda function to find square of a number
        mData = list(map(NumberMap,fData))

        print("List after map : ",mData)

        #lambda function for addition
        rData = reduce(NumberReduce,mData)

        print("Output of reduce : ", rData)


if __name__ == "__main__":
    main()

# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

# D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 4>python Assignment4_4.py
# Enter number of elements : 8
# 12
# 15
# 20
# 8
# 19
# 21
# 24
# 5
# Input List :  [12, 15, 20, 8, 19, 21, 24, 5]
# List after filter :  [12, 20, 8, 24]
# List after map :  [144, 400, 64, 576]
# Output of reduce :  1184