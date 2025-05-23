#Assignment 4 - Problem 3 - Filter map reduce to multiply numbers from list

from functools import reduce

NumberFilter = lambda num1 : num1 >= 70 and num1 <= 90

NumberMap = lambda num1 : num1+10

NumberReduce = lambda num1, num2 : num1 * num2

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

        #lambda function to filter numbers which >=70 && <=90
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


    # 3.Write a program which contains filter(), map() and reduce() in it. Python application which
    # contains one list of numbers. List contains the numbers which are accepted from user. Filter
    # should filter out all such numbers which greater than or equal to 70 and less than or equal to
    # 90. Map function will increase each number by 10. Reduce will return product of all that
    # numbers.
    # Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    # List after filter = [76, 89, 86, 90, 70]
    # List after map = [86, 99, 96, 100, 80]
    # Output of reduce = 6538752000


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 4>python Assignment4_3.py
    # Enter number of elements : 5
    # 69
    # 79
    # 70
    # 89
    # 91
    # Input List :  [69, 79, 70, 89, 91]
    # List after filter :  [79, 70, 89]
    # List after map :  [89, 80, 99]
    # Output of reduce :  704880
