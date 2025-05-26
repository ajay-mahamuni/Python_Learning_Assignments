#Assignment 11 - Problem 3 - Recursion function to sum of numbers

import sys

sum = 0

def CalculateSum(num):

    global sum

    if num > 0:
        sum = sum + num % 10
        num = num // 10
        CalculateSum(num)

    return sum
    
        


def main():
    inputNum = input("Enter a number : ")

    if inputNum.isdigit:
        ans = CalculateSum(int(inputNum))
        print("Sum of number ", inputNum, " is : ", ans)
    else:
        print("Enter valid number.")

if __name__ == "__main__":
    main()


    # 3. Sum of Digits
    # Write a recursive function to calculate the sum of digits of a number.
    # sum_of_digits(1234) → 10

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_3.py
    # Enter a number : 1250
    # Sum of number  1250  is :  8

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_3.py
    # Enter a number : 654321
    # Sum of number  654321  is :  21