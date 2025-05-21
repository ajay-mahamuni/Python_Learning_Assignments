#Assignment 3 - Problem 5 - Addition of prime numbers from number in a  list provided by user

from MarvellousNum import ChkPrime # type: ignore

from functools import reduce 

def ListPrime(num1,num2):
    return num1 + num2


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

        # use system function filter to get prime numbers only
        fData = list(filter(ChkPrime,dataList))

        rData = reduce(ListPrime,fData)

        print("Prime numbers : ", fData)

        print("Sum of Prime numbers : ", rData)

        # print("Frequency of ",numToSearch," from list is : ", cnt)

if __name__ == "__main__":
    main()



    # 5.Write a program which accept N numbers from user and store it into List. Return addition of all
    # prime numbers from that List. Main python file accepts N numbers from user and pass each
    # number to ChkPrime() function which is part of our user defined module named as
    # MarvellousNum. Name of the function from main python file should be ListPrime().
    # Input : Number of elements : 11
    # Input Elements : 13 5 45 7 4 56 10 34 2 5 8
    # Output : 54 (13 + 5 + 7 +2 + 5)


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 3>python Assignment3_5.py
    # Enter number of elements : 5
    # 12
    # 15
    # 17
    # 37
    # 45
    # Prime numbers :  [17, 37]
    # Sum of Prime numbers :  54