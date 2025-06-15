#Assignment 15 - Problem 3 - Python file i/o imlpmentation

import os
import sys
import datetime

def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("No file was provided in command line")
        exit()

    flag = os.path.exists(filename)

    if flag == True:
        fObj = open(filename,"r")        
        data = fObj.read()

        dateFormat = datetime.datetime.now()

        dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%X").replace(":","")

        newFileName = "Demo-" + dateFormat +".txt"

        cObj = open(newFileName,"w")

        cObj.write(data)

        print("New file created with name : ", newFileName)

        cObj.close()

        fObj.close()
        
    else:
        print("Provided file does not exist in directory")


if __name__ == "__main__":
    main()


    # 3.Write a program which accept file name from user and create new file named as Demo.txt and
    # copy all contents from existing file into new file. Accept file name through command line
    # arguments.
    # Input : ABC.txt
    # Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 15>python Assignment15_3.py Demo.txt
    # New file created with name :  Demo-12062025-181519.txt

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 15>python Assignment15_3.py Hello.txt
    # Provided file does not exist in directory