#Assignment 9 - Problem 2 - Multi threaded program to calculate square of number

import multiprocessing
import os

# NumberSquare = lambda num : print("Square of number : ", num , " is : ",num**2)

def NumberSquare(num,no):
    print("PID of Process",no," is : ", os.getpid())
    print("Square of number ", num , " is : ",num**2)
    print(end= " \n")


def main():

    numberList = input("Enter numbers separated by space: ")
     
    numberSplit = numberList.split()
     

    if len(numberSplit) > 1:
        try:    
            no = 1
            for i in numberSplit:                

                P1 = multiprocessing.Process(target=NumberSquare,args=(int(i),no))

                no = no + 1

                P1.start()

                P1.join()

        except Exception as ex:
            ("Error : ", ex)

    
    
if __name__ == "__main__":
    main()

    # 2. Write a Python program using multiprocessing.Process to square a list of
    # numbers using multiple processes.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 9>python Assignment9_2.py
    # Enter numbers separated by space: 10 20 30 40 50 60 70 80 90 100
    # PID of Process 1  is :  4480
    # Square of number  10  is :  100

    # PID of Process 2  is :  7612
    # Square of number  20  is :  400

    # PID of Process 3  is :  28092
    # Square of number  30  is :  900

    # PID of Process 4  is :  18648
    # Square of number  40  is :  1600

    # PID of Process 5  is :  28948
    # Square of number  50  is :  2500

    # PID of Process 6  is :  23336
    # Square of number  60  is :  3600

    # PID of Process 7  is :  10660
    # Square of number  70  is :  4900

    # PID of Process 8  is :  38972
    # Square of number  80  is :  6400

    # PID of Process 9  is :  11800
    # Square of number  90  is :  8100

    # PID of Process 10  is :  27948
    # Square of number  100  is :  10000