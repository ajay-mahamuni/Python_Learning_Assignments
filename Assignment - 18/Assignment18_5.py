#Assignment 18 - Problem 5 - Python file i/o imlpmentation

import os
import sys

def main():

    filename = input("Enter a filename :")

    textToSearch = input("Enter a word to search : ")

    flag = os.path.exists(filename)

    if flag == True:
        if len(textToSearch) == 0:
            print("Enter valid word to search")
            exit()
        else:
            fObj = open(filename,"r")

            data = fObj.read()

            data = data.lower()

            textToSearch = textToSearch.lower()

            index = data.count(textToSearch)

            print("Frequency of string ",textToSearch, " is : ",index)

            fObj.close()

    else:
        print("Provided file does not exist in directory")
        exit()


if __name__ == "__main__":
    main()


    # 5. Accept file name and one string from user and return the frequency of that string from file.
    # Input : Demo.txt Marvellous
    # Search “Marvellous” in Demo.txt

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 18>python Assignment18_5.py
    # Enter a filename :Demo.txt
    # Enter a word to search : Nature
    # Frequency of string  nature  is :  5