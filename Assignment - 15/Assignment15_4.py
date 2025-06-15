#Assignment 15 - Problem 4 - Python file i/o imlpmentation

import os
import sys

def main():

    if len(sys.argv) > 1 and len(sys.argv) > 2:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
    else:
        print("No file was provided in command line")
        exit()

    flag1 = os.path.exists(file1)
    flag2 = os.path.exists(file2)

    if flag1 == True and flag2 == True:
        f1Obj = open(file1,"r")        
        data1 = f1Obj.read()

        f2Obj = open(file2,"r")        
        data2 = f2Obj.read()

        if data1 == data2:
            print("Content of both files are same..")
        else:
            print("Content of both files are not same..")

        
        f1Obj.close()

        f2Obj.close()
        
    else:
        print("Provided file does not exist in directory")


if __name__ == "__main__":
    main()


    # 4.Write a program which accept two file names from user and compare contents of both the
    # files. If both the files contains same contents then display success otherwise display failure.
    # Accept names of both the files from command line.
    # Input : Demo.txt Hello.txt
    # Compare contents of Demo.txt and Hello.txt


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 15>python Assignment15_4.py Demo.txt Demo-12062025-181519.txt
    # Content of both files are same..

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 15>python Assignment15_4.py Demo.txt Assignment15_1.py
    # Content of both files are not same..

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 15>python Assignment15_4.py Demo.txt
    # No file was provided in command line