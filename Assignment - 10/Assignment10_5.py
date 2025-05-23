#Assignment 4 - Problem 5 - Filter map reduce to calculate multiplication by 2 to prime numbers from list

from functools import reduce

def NumberFilter(num):
    flag = True

    if num == 0 or num == 1: 
        flag = False
    elif num > 1:      
        for no in range(2,num):
            if(num % no) == 0:
                flag = False
                break

    return flag

NumberMap = lambda num1 : num1 * 2

NumberReduce = lambda num1, num2 : num1 if (num1 > num2) else num2

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

        #lambda function to find prime number
        fData = list(filter(NumberFilter,dataList))

        print("List after filter : ",fData)

        #lambda function to increase value by 10
        mData = list(map(NumberMap,fData))

        print("List after map : ",mData)

        #lambda function to multiplication
        rData = reduce(NumberReduce,mData)

        print("Output of reduce : ", rData)


if __name__ == "__main__":
    main()

    # 5.Write a program which contains filter(), map() and reduce() in it. Python application which
    # contains one list of numbers. List contains the numbers which are accepted from user. Filter
    # should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
    # return Maximum number from that numbers. (You can also use normal functions instead of
    # lambda functions).
    # Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
    # List after filter = [2, 11, 17, 23, 31]
    # List after map = [4, 22, 34, 46, 62]
    # Output of reduce = 62


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 4>python Assignment4_5.py
    # Enter number of elements : 8
    # 2
    # 11
    # 17
    # 19
    # 12
    # 18
    # 89
    # 16
    # Input List :  [2, 11, 17, 19, 12, 18, 89, 16]
    # List after filter :  [2, 11, 17, 19, 89]
    # List after map :  [4, 22, 34, 38, 178]
    # Output of reduce :  178