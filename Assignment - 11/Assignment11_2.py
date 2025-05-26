#Assignment 11 - Problem 2 - Recursion function tofind factorial of number

import sys

cntr = 1

def Display(num):

    global cntr

    if  cntr <= num :
        if  num % cntr == 0:
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


    # 2. Factorial Using Recursion
    # Write a recursive function to calculate factorial of a number.
    # factorial(5) → 120


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_2.py
    # Enter a number : 10
    # 1 2 5 10
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_2.py
    # Enter a number : 25
    # 1 5 25
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_2.py
    # Enter a number : 100
    # 1 2 4 5 10 20 25 50 100