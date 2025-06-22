#Assignment 19 - Problem 1 - Python automation of files and directories

import os
import sys
import time
import datetime



def DirectoryWatcher(dirName,fileExtension):
    
    flag = os.path.isabs(dirName)

    if flag == False:
        dirName = os.path.abspath(dirName)

    flag = os.path.exists(dirName)

    if flag == False:
        print("Path is invalid.")
        exit()

    flag = os.path.isdir(dirName)

    if flag == False:
        print("Provided path is not a directory")
        exit()

    
    # print("Aboslute path : ", dirName)

    for folderName, subfolderNames,filenames in os.walk(dirName):
        for fname in filenames:            
            if fname.endswith(fileExtension):
                print("Filename : ", fname,end="\n")
            

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This application searches files with specific extension")
        elif len(sys.argv) > 1 and (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script...")
            print("Scriptname.py NameOfDirectory File extension")
            print("Please provide valid absolute path")
        else:
            print("Enter valid arguments")
            print("Use below keywords: ")
            print("--h / --H : To get help ")
            print("--u / --U : To know how to use script ")

    elif len(sys.argv) == 3:
         DirectoryWatcher(sys.argv[1],sys.argv[2])
    else:
        print("Enter valid arguments")
        print("Use below keywords: ")
        print("--h / --H : To get help ")
        print("--u / --U : To know how to use script ")


if __name__ == "__main__":
    main()



    # 1.Design automation script which accept directory name and file extension from user. Display all
    # files with that extension.
    # Usage : DirectoryFileSearch.py “Demo” “.txt”
    # Demo is name of directory and .txt is the extension that we want to search.


    
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19>python Assignment19_1.py Marvellous txt
    # Filename :  Test1.txt
    # Filename :  Test2.txt
    # Filename :  Test3.txt
    # Filename :  Test4.txt

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19>python Assignment19_1.py Marvellous py
    # Filename :  Test1.py
    # Filename :  Test2.py
    # Filename :  Test3.py
    # Filename :  Test4.py

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19>python Assignment19_1.py Marvellous
    # Enter valid arguments
    # Use below keywords:
    # --h / --H : To get help
    # --u / --U : To know how to use script

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19>python Assignment19_1.py --H
    # This application searches files with specific extension

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19>python Assignment19_1.py --u
    # Usage of script...
    # Scriptname.py NameOfDirectory File extension
    # Please provide valid absolute path