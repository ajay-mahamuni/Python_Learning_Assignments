#Assignment 11 - Problem 1 - Recursion to print numbers

import sys

cntr = 1

def Display(num):

    global cntr

    if cntr <= num:
        print(cntr, end=" ")
        cntr = cntr + 1
        Display(num)


def main():
    inputNum = input("Enter a number : ")

    if inputNum.isdigit:
        Display(int(inputNum))
    else:
        print("Enter valid number.")

    
if __name__ == "__main__":
    main()



    # 1. Print Numbers Using Recursion
    # Write a recursive function to print numbers from 1 to N.
    # Expected Output (for n=5):
    # 1 2 3 4 5


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_1.py
    # Enter a number : 5
    # 1 2 3 4 5
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_1.py
    # Enter a number : 11
    # 1 2 3 4 5 6 7 8 9 10 11