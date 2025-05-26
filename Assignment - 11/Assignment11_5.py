#Assignment 11 - Problem 5 - Recursion to count number of zero's in a number


import sys

sum = 0

def CountZero(num):

    global sum
    
    if num > 0:
        if num % 10 == 0:            
            sum = sum + 1
        
        num = num // 10
        CountZero(num)

    return sum
    
        


def main():

    inputNum = input("Enter a number : ")

    if  inputNum.isdigit:
        if int(inputNum) > 0:
            ans = CountZero(int(inputNum))
        else : ans = 1
        print("Number of zero's in number ", inputNum, " is : ", ans)
    else:
        print("Enter valid number.")

if __name__ == "__main__":
    main()


    # 5. Count Zeros in a Number (Recursively)
    # Write a recursive function to count how many zeros are in the given number.
    # count_zeros(1020300) → 4


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_5.py
    # Enter a number : 100
    # Number of zero's in number  100  is :  2

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_5.py
    # Enter a number : 10
    # Number of zero's in number  10  is :  1

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 11>python Assignment11_5.py
    # Enter a number : 0
    # Number of zero's in number  0  is :  1