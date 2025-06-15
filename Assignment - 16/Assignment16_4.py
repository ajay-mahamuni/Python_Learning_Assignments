#Assignment 15 - Problem 4 - Python file i/o imlpmentation

import os

def main():    
    
    data = []
    print("Enter 10 numbers names : ")
    
    fObj = open("Numbers.txt","w")

    

    for i in range(10):
        fObj.write(input()+"\n")    

    fObj.close()

    print("File created with name : Numbers.txt")

if __name__ == "__main__":
    main()


    # 4. Accept 10 numbers from the user and write them into a file named numbers.txt,
    # each on a new line.

    
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_4.py
    # Enter 10 numbers names :
    # 11
    # 21
    # 51
    # 101
    # 151
    # 201
    # 251
    # 501
    # 1001
    # 1111
    # File created with name : Numbers.txt