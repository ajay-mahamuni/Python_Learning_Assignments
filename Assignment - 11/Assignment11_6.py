#Assignment 11 - Problem 6 - Recursion to perform sum of given numbers

import sys

sum = 0

def CalculateSum(num):
    global sum
    
    if num > 0:
        sum = sum + num
        num = num - 1
        CalculateSum(num)

    return sum

        


def main():
    inputNum = input("Enter a number : ")

    if inputNum.isdigit():
        ans = CalculateSum(int(inputNum))
        print("Sum of natural numbers is : ", ans)
    else:
        print("Enter valid number..")

if __name__ == "__main__":    
    main()



    # 6. Sum of First N Natural Numbers
    # Write a recursive function to calculate sum from 1 to n.
    # sum_n(5) → 15

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_6.py
    # Enter a number : 15
    # Sum of natural numbers is :  120

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_6.py
    # Enter a number : 10
    # Sum of natural numbers is :  55

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_6.py
    # Enter a number : 99
    # Sum of natural numbers is :  4950