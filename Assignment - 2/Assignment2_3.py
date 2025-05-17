#Assignment 2 - Problem 3 - For loop to calculate factorial of number

def forloop(number):
    
    result = 1

    for no in range(number,0,-1):
        result = result * no

    print("Factorial of number ",number, " is : ", result) 

def main():

    num = int(input("Enter a number : "))

    forloop(num)

if __name__ == "__main__":
    main()

#3. Write a program which accept one number from user and return its factorial.
# Input : 5 Output : 120

#D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_3.py
# Enter a number : 5
# Factorial of number  5  is :  120