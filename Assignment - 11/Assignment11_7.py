#Assignment 11 - Problem 7 - Recursion to print numbers

import threading
import multiprocessing
import sys

cntr = 1

def DisplayStar(num):
    global cntr

    
    
    if cntr <= num:
        print("*" * cntr, end = " \n")
        cntr = cntr + 1

    P1 = multiprocessing.Process(target=DisplayStar,args=(num,))
    P1.start()

        
        


def main():
    inputNum = input("Enter a number : ")

    if inputNum.isdigit():
        DisplayStar(int(inputNum))        
    else:
        print("Enter valid number..")

if __name__ == "__main__":    
    main()



    # 7. Print Pattern Using Recursion (Right Triangle)
    # Write a recursive function to print the following pattern:
    # *
    # * *
    # * * *
    # * * * *

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_7.py
    # Enter a number : 10
    # *
    # **
    # ***
    # ****
    # *****
    # ******
    # *******
    # ********
    # *********
    # **********

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_7.py
    # Enter a number : 7
    # *
    # **
    # ***
    # ****
    # *****
    # ******
    # *******