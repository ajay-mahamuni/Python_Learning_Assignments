#Assignment 8 - Problem 3 - Multi threaded program for sum of even and odd numbers from given list of numbers

import threading
import os
import sys


CheckEven = lambda num : True if num % 2 == 0 else False

def EvenFactor(dataList):    

    try:
        result = 0
        datalist= []

        for i in dataList:
            i = int(i)
            if CheckEven(i): #check the value is factor of given number and is an even number then add to list
                datalist.append(i)

                result = result + i
        
        print("Even Factors : ", datalist)
        
        print("Sum of Even Factors : ", result)

    except Exception as ex:
        print("Error : ", ex)

def OddFactor(dataList):

    try:
        
        result = 0
        datalist= []

        for i in dataList:
            i = int(i)
            if CheckEven(i) == False: #check the value is factor of given number and is an odd number then add to list
                datalist.append(i)

                result = result + i
        
        print("Odd Factors : ", datalist)
        
        print("Sum of Odd Factors : ", result)

    except Exception as ex:
        print("Error : ", ex)


        

def main():   

    numberList = input("Enter numbers separated by space: ")
     
    numberSplit = numberList.split()
     

    if len(numberSplit) > 1:

        try:
        
            T1 = threading.Thread(target=EvenFactor,args=(numberSplit,))

            T2 = threading.Thread(target=OddFactor,args=(numberSplit,))

            T1.start()

            T2.start()

            T1.join()

            T2.join()

        except Exception as exObj:
            print("Exception occured : ",exObj)

    else:
        print("Enter valid number..")


    
if __name__ == "__main__":
    main()

    # 3.Design python application which creates two threads as evenlist and oddlist. Both the
    # threads accept list of integers as parameter. Evenlist thread add all even elements
    # from input list and display the addition. Oddlist thread add all odd elements from input
    # list and display the addition.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 8>python Assignment8_3.py
    # Enter numbers separated by space: 1 2 3 4 5 6 7 8 9 10
    # Even Factors :  [2, 4, 6, 8, 10]
    # Sum of Even Factors :  30
    # Odd Factors :  [1, 3, 5, 7, 9]
    # Sum of Odd Factors :  25