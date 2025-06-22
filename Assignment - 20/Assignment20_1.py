#Assignment 20 - Problem 1 - Python automation of files and directories

import os
import sys
import hashlib


def DirectoryWatcher(dirName):
    
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
                fname = os.path.join(dirName,fname)
                hexResult = CalculateCheckSum(fname,1024)
                print("Checksum of file is : ", hexResult,end="\n")



def CalculateCheckSum(filePath,blockSize=1024):
    fObj = open(filePath,"rb")

    hObj = hashlib.md5()

    buffer = fObj.read(blockSize)

    while (len(buffer) > 0):
        hObj.update(buffer)
        buffer = fObj.read(blockSize)

    fObj.close()

    return hObj.hexdigest()
            

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This application searches files with checksum")
        elif len(sys.argv) > 1 and (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script...")
            print("Scriptname.py NameOfDirectory ")
            print("Please provide valid absolute path")
        else:
            DirectoryWatcher(sys.argv[1])            
    else:
        print("Enter valid arguments")
        print("Use below keywords: ")
        print("--h / --H : To get help ")
        print("--u / --U : To know how to use script ")


if __name__ == "__main__":
    main()



    # 1.Design automation script which accept directory name and display checksum of all files.
    # Usage : DirectoryChecksum.py “Demo”
    # Demo is name of directory.

    
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 20>python Assignment20_1.py Marvellous
    # Checksum of file is :  eb2e81c8b545b7ff5b63b71bcee954f0
    # Checksum of file is :  971459d088f152f9bce2f1a5ebf75099
    # Checksum of file is :  458af2cf975f6ab1c0273bd658119542
    # Checksum of file is :  7be378367abff2b42653b7f293ac0ea8
    # Checksum of file is :  1b62c6de0a18842ff4bc3c39f5d358de
    # Checksum of file is :  e96a5d0feab783f98bf9164b387b64a3

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 20>python Assignment20_1.py Demo
    # Path is invalid.