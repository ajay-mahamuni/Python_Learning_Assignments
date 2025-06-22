#Assignment 20 - Problem 3 - Python automation of files and directories

import os
import sys
import hashlib
import time
import datetime


def FindDuplicate(dirName):
    
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

    duplicateFiles = {}    
    
    for folderName, subfolderNames,filenames in os.walk(dirName):
        for fname in filenames:
                fname = os.path.join(dirName,fname)
                hexResult = CalculateCheckSum(fname,1024)
                if hexResult in duplicateFiles:
                    duplicateFiles[hexResult].append(fname)
                else:
                    duplicateFiles[hexResult] = [fname]

    return duplicateFiles

def DeleteDuplicateFiles(duplicateFilesDict):
    totalFileCount = 0
    deletedFileCount = 0
    result = list(filter(lambda x: len(x)>1,duplicateFilesDict.values()))

    cnt = 0
    deletedFileCount = 0
    duplicateFiles = []
    for value in result:
        for subValue in value:
            cnt = cnt + 1
            if cnt > 1:
                os.remove(subValue)
                duplicateFiles.append(subValue)
                deletedFileCount = deletedFileCount + 1

        cnt = 0
    
    print("Total deleted files : ",deletedFileCount)

    CreateLog(duplicateFiles)




def CalculateCheckSum(filePath,blockSize=1024):
    fObj = open(filePath,"rb")

    hObj = hashlib.md5()

    buffer = fObj.read(blockSize)

    while (len(buffer) > 0):
        hObj.update(buffer)
        buffer = fObj.read(blockSize)

    fObj.close()

    return hObj.hexdigest()


def CreateLog(logData):
    dateFormat = datetime.datetime.now()
    dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%H%M").replace(":","")

    fileName = "MarvellousLog%s.log" %(dateFormat)
    fileName = fileName.replace(":","")
    fileName = fileName.replace(" ","_")
    

    print("Log file for deleted Duplicate files with names : ", fileName," is created.")

    fObj = open(fileName,"w")

    border = "-"*80 + "\n"
    fObj.write(border)
    fObj.write("---------------------------Deleted Duplicate File Logs-------------------------- \n")
    fObj.write(border)

    for values in logData:
        fObj.write("%s \n" %values)

    fObj.write("Log file created at : "+ time.ctime()+"\n")
    fObj.write(border)

    fObj.close()
            

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This application searches files with checksum")
        elif len(sys.argv) > 1 and (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script...")
            print("Scriptname.py NameOfDirectory ")
            print("Please provide valid absolute path")
        else:
            result = FindDuplicate(sys.argv[1])
            DeleteDuplicateFiles(result)            
    else:
        print("Enter valid arguments")
        print("Use below keywords: ")
        print("--h / --H : To get help ")
        print("--u / --U : To know how to use script ")


if __name__ == "__main__":
    main()



    # 3. Design automation script which accept directory name and delete all duplicate files from that
    # directory. Write names of duplicate files from that directory into log file named as Log.txt.
    # Log.txt file should be created into current directory.
    # Usage : DirectoryDusplicateRemoval.py “Demo”
    # Demo is name of directory.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 20>python Assignment20_3.py Marvellous
    # Total deleted files :  3
    # Log file for deleted Duplicate files with names :  MarvellousLog22062025-0048.log  is created.