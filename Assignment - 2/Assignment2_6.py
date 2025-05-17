#Assignment 2 - Problem 6 - For loop

def forloop(number):
    
    for no in range(number,0,-1):
        print("*" * no)
    
def main():

    num = int(input("Enter a number : "))

    forloop(num)

if __name__ == "__main__":
    main()

    #6. Write a program which accept one number and display below pattern.
    #Input : 5
    #Output : 
    # * * * * *
    # * * * *
    # * * *
    # * *
    # *

    #D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_6.py
    # Enter a number : 5
    # *****
    # ****
    # ***
    # **
    # *