#Assignment 9 - Problem 3 - Multi threaded program to find factors of numbers in list

import multiprocessing

def NumberFactor(num):
    num = int(num)
    dataList = []
    
    for i in range(1,num):
        if num % i == 0:
            dataList.append(i)

    print("Factors of ",num, " are : ", dataList,end= " \n")

    return dataList


def main():

    numberList = input("Enter numbers separated by space: ")

    numberSplit = numberList.split()

    print("Input : ", numberSplit)

    result = []

    p = multiprocessing.Pool()
    
    result = p.map(NumberFactor,numberSplit)

    print("Output : ", result)
    
if __name__ == "__main__":
    main()

    # 3. Create a Python program that uses multiprocessing.Pool to compute
    # factorial of numbers in a list.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 9>python Assignment9_3.py
    # Enter numbers separated by space: 20 30 40 50 60
    # Input :  ['20', '30', '40', '50', '60']
    # Factors of  20  are :  [1, 2, 4, 5, 10]
    # Factors of  30  are :  [1, 2, 3, 5, 6, 10, 15]
    # Factors of  40  are :  [1, 2, 4, 5, 8, 10, 20]
    # Factors of  50  are :  [1, 2, 5, 10, 25]
    # Factors of  60  are :  [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30]
    # Output :  [[1, 2, 4, 5, 10], [1, 2, 3, 5, 6, 10, 15], [1, 2, 4, 5, 8, 10, 20], [1, 2, 5, 10, 25], [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30]]