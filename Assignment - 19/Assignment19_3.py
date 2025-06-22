#Assignment 19 - Problem 3 - Python automation of files and directories

import os
import sys
import shutil


def CreateFilesAtNewDir(dirName,newDir):
    
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

    # if directory already exist then delete files inside that folder else create new directory
    if os.path.exists(newDir) == True:
        for folderName, subfolderNames,filenames in os.walk(newDir):
            for fname in filenames:
                fname = os.path.join(newDir,fname)
                os.remove(fname)
    else:
        os.makedirs(newDir)


    newDirPath = os.path.abspath(newDir)

    for folderName, subfolderNames,filenames in os.walk(dirName):
        for fname in filenames:                                        
                newFilePath = os.path.join(newDirPath,fname)
                fname = os.path.join(dirName,fname)
                shutil.copyfile(fname,newFilePath)
                print("New Filename : ", newFilePath,end="\n")
            

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
         CreateFilesAtNewDir(sys.argv[1],sys.argv[2])
    else:
        print("Enter valid arguments")
        print("Use below keywords: ")
        print("--h / --H : To get help ")
        print("--u / --U : To know how to use script ")


if __name__ == "__main__":
    main()


    # 3. Design automation script which accept two directory names. Copy all files from first directory
    # into second directory. Second directory should be created at run time.
    # Usage : DirectoryCopy.py “Demo” “Temp”
    # Demo is name of directory which is existing and contains files in it. We have to create new
    # Directory as Temp and copy all files from Demo to Temp.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19>python Assignment19_3.py Marvellous Temp
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test1.java
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test1.py
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test1.txt
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test2.java
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test2.py
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test2.txt
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test3.java
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test3.py
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test3.txt
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test4.java
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test4.py
    # New Filename :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 19\Temp\Test4.txt