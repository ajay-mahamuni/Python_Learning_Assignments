#Assignment 20 - Problem 2 - Python automation of files and directories

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
    

    print("Log file with Duplicate file names : ", fileName," created.")

    result = list(filter(lambda x: len(x)>1,logData.values()))

    fObj = open(fileName,"w")
    border = "-"*80 + "\n"
    fObj.write(border)
    fObj.write("-------------------------------Duplicate File Logs------------------------------ \n")
    fObj.write(border)

    counter = 0
    for values in result:
        for subValue in values:
            fObj.write("%s \n" %subValue)
            counter = counter + 1

    print("Duplicate file count : ",counter)

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
            CreateLog(result)
    else:
        print("Enter valid arguments")
        print("Use below keywords: ")
        print("--h / --H : To get help ")
        print("--u / --U : To know how to use script ")


if __name__ == "__main__":
    main()



    # 2. Design automation script which accept directory name and write names of duplicate files from
    # that directory into log file named as Log.txt. Log.txt file should be created into current
    # directory.
    # Usage : DirectoryDusplicate.py “Demo”


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 20>python Assignment20_2.py Marvellous
    # Log file with Duplicate file names :  MarvellousLog22062025-0013.log  created.