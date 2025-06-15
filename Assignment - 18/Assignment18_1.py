#Assignment 18 - Problem 1 - Python file i/o imlpmentation

import os

def main():
    filename = input("Enter a filename :")

    flag = os.path.exists(filename)

    if flag == True:
        print("Provided file exist in directory")
    else:
        print("Provided file does not exist in directory")


if __name__ == "__main__":
    main()


    # 1.Write a program which accepts file name from user and check whether that file exists in
    # current directory or not.
    # Input : Demo.txt
    # Check whether Demo.txt exists or not.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 18>python Assignment18_1.py
    # Enter a filename :Demo.txt
    # Provided file exist in directory

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 18>python Assignment18_1.py
    # Enter a filename :Hello.txt
    # Provided file does not exist in directory

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 18>python Assignment18_1.py
    # Enter a filename :Assignment18_1.py
    # Provided file exist in directory
