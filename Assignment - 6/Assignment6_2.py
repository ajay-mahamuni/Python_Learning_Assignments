#Assignment 6 - Problem 2 - Sum of even numbers using for loop

def CheckEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def Sum(num1, num2):
    return num1 + num2

def main():

    result = 0

    print("Even numbers : ")

    for i in range(1,100):
        if CheckEven(i):
            result = result + i
            print(i, end = " ")


    print("\n Sum of even numbers is : ", result)

if __name__ == "__main__":
    main()


    # Q2. Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum
    # of all even numbers from 1 to 100.
    # Expected Output:
    # Sum of even numbers between 1 to 100 is: 2550


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_2.py
    # Even numbers :
    # 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98
    # Sum of even numbers is :  2450

    