#Assignment 11 - Problem 4 - Recursion function power of number

import sys

powerOfNumber = 1
cntr = 1

def CalculatePower(num,powerNumber):

    global powerOfNumber
    global cntr

    if cntr <= powerNumber:
        powerOfNumber = powerOfNumber * num
        cntr = cntr + 1
        CalculatePower(num,powerNumber)

    return powerOfNumber
    
        


def main():
    inputNum = input("Enter a number : ")

    powerNum = input("Enter power of number : ")

    if inputNum.isdigit and powerNum.isdigit:
        ans = CalculatePower(int(inputNum),int(powerNum))
        print("Sum of number ", inputNum, " is : ", ans)
    else:
        print("Enter valid number.")

if __name__ == "__main__":
    main()


    # 4. Power Function Using Recursion
    # Write a recursive function to calculate x^n.
    # power(2, 3) → 8

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_4.py
    # Enter a number : 2
    # Enter power of number : 4
    # Sum of number  2  is :  16

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_4.py
    # Enter a number : 10
    # Enter power of number : 4
    # Sum of number  10  is :  10000