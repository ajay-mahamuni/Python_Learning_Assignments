#Assignment 15 - Problem 3 - Python file i/o imlpmentation

import os

def main():    
    
    fObj = open("Student.txt","r")

    rdata = fObj.read()

    lines = rdata.split() 

    cnt = 0

    leng = len(rdata)

    for word in lines:
        cnt = cnt + 1

    fObj.close()

    fObj = open("Student.txt","r")

    rdata = fObj.readlines()

    numberOfLines = len(rdata)

    print("Number of lines in a file : ", numberOfLines)

    print("Number of words in a file : ", cnt)

    print("Number of characters in a file : ", leng)

    fObj.close()

if __name__ == "__main__":
    main()


    # 3. Write a Python script to count the number of lines, words, and characters in a
    # given file.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_3.py
    # Number of lines in a file :  5
    # Number of words in a file :  10
    # Number of characters in a file :  75