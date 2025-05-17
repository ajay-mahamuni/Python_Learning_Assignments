#Assignment 2 - Problem 4 - For loop to calculate addition of factors of given number

def forloop(number):
    
    result = 0
    for no in range(number-1,0,-1):
        if number % no == 0:
            result = result + no

    print("Addition of factor of number  ",number, " is : ", result) 

def main():
    
    num = int(input("Enter a number : "))

    forloop(num)

if __name__ == "__main__":
    main()

    #4.Write a program which accept one number form user and return addition of its factors.
    # Input : 12 Output : 16 (1+2+3+4+6)

    #D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_4.py
    # Enter a number : 12
    # Addition of factor of number   12  is :  16
