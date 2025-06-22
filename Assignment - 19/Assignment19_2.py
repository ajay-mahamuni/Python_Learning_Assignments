#Assignment 19 - Problem 2 - Python automation of files and directories

import os
import sys


def DirectoryWatcher(dirName,fileExtension,extensionToReplace):
    
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

    
    
    for folderName, subfolderNames,filenames in os.walk(dirName):
        for fname in filenames:            
            if fname.endswith(fileExtension):
                fname = os.path.join(folderName,fname)

                print("Old file name : ", fname)

                basePath = os.path.splitext(fname)                
                newFilePath = basePath[0] + "." + extensionToReplace
                os.rename(fname,newFilePath)

    for folderName, subfolderNames,filenames in os.walk(dirName):
        for fname in filenames:            
            if fname.endswith(extensionToReplace):
                fname = os.path.join(folderName,fname)

                print("New file name : ", fname)
            

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This application searches files with specific extension")
        elif len(sys.argv) > 1 and (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script...")
            print("Scriptname.py NameOfDirectory File extension to search File extension to replace with")
            print("Please provide valid absolute path")
        else:
            print("Enter valid arguments")
            print("Use below keywords: ")
            print("--h / --H : To get help ")
            print("--u / --U : To know how to use script ")

    elif len(sys.argv) == 4:
         DirectoryWatcher(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print("Enter valid arguments")
        print("Use below keywords: ")
        print("--h / --H : To get help ")
        print("--u / --U : To know how to use script ")


if __name__ == "__main__":
    main()



    # 2. Design automation script which accept directory name and two file extensions from user.
    # Rename all files with first file extension with the second file extenntion.
    # Usage : DirectoryRename.py “Demo” “.txt” “.doc”
    # Demo is name of directory and .txt is the extension that we want to search and rename
    # with .doc.
    # After execution this script each .txt file gets renamed as .doc.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19>python Assignment19_2.py Marvellous cofig py
    # Old file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test1.cofig
    # Old file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test2.cofig
    # Old file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test3.cofig
    # Old file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test4.cofig
    # New file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test1.py
    # New file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test2.py
    # New file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test3.py
    # New file name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Marvellous\Test4.py