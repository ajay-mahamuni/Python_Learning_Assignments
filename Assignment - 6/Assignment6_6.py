#Assignment 6 - Problem 6 - Print Triangle format


def main():
    
    num = input("Enter a number : ")
    

    if num.isdigit():

        num = int(num)

        for i in range(num):
            for j in range(i+1):
                print("*", end = " ")
            print(end = " \n")
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()

    # Q6. Print Triangle Pattern using Nested Loops
    # Expected Output:

    # *
    # * *
    # * * *
    # * * * *


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_6.py
    # Enter a number : 9
    # *
    # * *
    # * * *
    # * * * *
    # * * * * *
    # * * * * * *
    # * * * * * * *
    # * * * * * * * *
    # * * * * * * * * *

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_6.py
    # Enter a number : 4
    # *
    # * *
    # * * *
    # * * * *

