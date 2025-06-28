import os
import sys
import time
import hashlib 
import schedule
import datetime
import EmailModule # type: ignore

def CalculateCheckSumCopy(filePath, blockSize = 1024):
    fileObjet = open(filePath, "rb")
    fileObjet = hashlib.md5()
    buffer = fileObjet.read(blockSize)
    
    while (len(buffer) > 0):
        fileObjet.update(buffer)
        buffer = fileObjet.read(blockSize)

    fileObjet.close()

    return fileObjet.hexdigest()

def CalculateCheckSum(filePath,blockSize=1024):
    fObj = open(filePath,"rb")

    hObj = hashlib.md5()

    buffer = fObj.read(blockSize)

    while (len(buffer) > 0):
        hObj.update(buffer)
        buffer = fObj.read(blockSize)

    fObj.close()

    return hObj.hexdigest()


def FindDuplicateSendLogs(folderPath,emailofReceiver):

    startTime = datetime.datetime.now()

    flag = os.path.isabs(folderPath)

    if flag == False:
        flag = os.path.abspath(folderPath)

    flag = os.path.exists(folderPath)

    if flag == False:
        print("Provided folder path is invalid.")
        exit()

    flag = os.path.isdir(folderPath)

    if flag == False:
        print("Provided folder path is not a directory.")
        exit()

    duplicateFilesDict = {}

    for folderName, subFolderNames, fileNames in os.walk(folderPath):        
            
            folderFullPath = os.path.abspath(folderName)
            for fName in fileNames:            
                
                fName = os.path.join(folderFullPath,fName)
                
                checkSumResult = CalculateCheckSum(fName)

                if checkSumResult in duplicateFilesDict:
                    duplicateFilesDict[checkSumResult].append(fName)
                else:
                    duplicateFilesDict[checkSumResult] = [fName]
    
    totalFileCount = 0

    for x in duplicateFilesDict:
        totalFileCount = totalFileCount + len(duplicateFilesDict[x])
    
    duplicateFiles = DeleteDuplicateFiles(duplicateFilesDict)
    
    CreateLogAndSendEmail("Marvellous",duplicateFiles,totalFileCount,emailofReceiver,startTime)
    



def DeleteDuplicateFiles(duplicateFileDict):
    counter = 0
    totalFileCount = 0
    deletedFileCount = 0
    duplicateFiles = []

    result = list(filter(lambda x : len(x) > 1, duplicateFileDict.values()))

    for values in result:
        for subValue in values:
            counter = counter + 1
            
            if counter > 1:
                fileCreateDatetime = GetFileCreationDateTime(subValue)
                fileDetails = subValue + "\t\t\t" + str(fileCreateDatetime)
                duplicateFiles.append(fileDetails)
                os.remove(subValue)
                deletedFileCount = deletedFileCount + 1

        counter = 0    

    return duplicateFiles


def GetFileCreationDateTime(filePath):
    
    fileCreationTimeStamp = os.path.getctime(filePath)

    creationDateTime = datetime.datetime.fromtimestamp(fileCreationTimeStamp)

    return creationDateTime

def CreateLogAndSendEmail(folderName,logData,totalScannedFiles,emailAddress,startTime):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    dateFormat = datetime.datetime.now()
    dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%H%M").replace(":","")

    fileName = "MarvellousLog%s.log" %(dateFormat)
    fileName = fileName.replace(":","")
    fileName = fileName.replace(" ","_")

    fileName = os.path.join(folderName,fileName)    

    fObj = open(fileName,"w")

    border = "-"*140 + "\n"
    fObj.write(border)
    fObj.write("Process Monitoring Logs \n")
    fObj.write(border)
    fObj.write("Deleted File Name \t\t\t\t\t\t")
    fObj.write("File Creation Datetime \n")
    fObj.write(border)

    
    for values in logData:
        fObj.write("%s \n" %values)
    fObj.write("Log file created at : "+ time.ctime()+"\n")

    deletedFileCount = len(logData)

    endTime = datetime.datetime.now()
    totalTime = endTime - startTime
    fObj.write("Time taken by process to delete duplciate files :" + str(totalTime) + "\n")    

    fObj.write(border)
    fObj.close()

    fileName = os.path.abspath(fileName)

    emailBody = "Hello There, \n This email contains summary of Automation process for deleting ducplicate files of a particular directory.\n Below are the details of summary and log file is attached for your reference." 
    emailBody = emailBody + "Total files scanned : " + str(totalScannedFiles) + "\n"
    emailBody = emailBody + "Duplicate deleted files : " + str(deletedFileCount) + "\n"
    emailBody = emailBody + "Process start time : " + str(startTime) + "\n"
    emailBody = emailBody + "Process end time : " + str(endTime) + "\n"
    emailBody = emailBody + "Total time taken by the process to complete the task : " + str(totalTime) + "\n"
    emailBody = emailBody + "Please find attached log of all duplicate files deleted by automation process."

    subject = "Duplicate File Log"    
    
    SendEmail(subject, emailBody, fileName,emailAddress)

    Display(fileName,totalScannedFiles,deletedFileCount,startTime,endTime,totalTime,emailAddress)


def SendEmail(subject, emailBody, attachmentFilePath,receiverEmail):
    EmailModule.send_email_using_gmail(subject, emailBody, attachmentFilePath,receiverEmail)

def Display(fileName,totalScannedFiles,deletedFileCount,startTime,endTime,totalTime,emailAddress):    
    print("Total files scanned : " + str(totalScannedFiles) + "\n")
    print("Duplicate deleted files : " + str(deletedFileCount) + "\n")
    print("Process start time : " + str(startTime) + "\n")
    print("Process end time : " + str(endTime) + "\n")
    print("Total time taken by the process to complete the task : " + str(totalTime) + "\n")
    print("Log file created with name : ", fileName + "\n")


def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This application searches duplicate files and delete them send list of duplicate file list to provided email address.")
        elif len(sys.argv) > 1 and (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script...")
            print("Scriptname.py NameOfDirectory IntervalinMinutes EmailofReceiver")
    if len(sys.argv) == 4:
        minuteInterval = sys.argv[2]
        if minuteInterval.isdigit():            
            folderPath = sys.argv[1]
            emailofReceiver = sys.argv[3]
            
            schedule.every(int(minuteInterval)).minutes.do(FindDuplicateSendLogs,folderPath,emailofReceiver)

            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            print("Enter valid minutes interval.")
            exit()
        

            

if __name__ == "__main__":
    main()


    # Design automation script which performs following task.
    # Accept Directory name from user and delete all duplicate files from the specified directory by
    # considering the checksum of files.
    # Create one Directory named as Marvellous and inside that directory create log file which
    # maintains all names of duplicate files which are deleted.
    # Name of that log file should contains the date and time at which that file gets created.
    # Accept duration in minutes from user and perform task of duplicate file removal after the specific
    # time interval.
    # Accept Mail id from user and send the attachment of the log file.
    # Mail body should contains statistics about the operation of duplicate file removal.
    # Mail body should contains below things :
    # Starting time of scanning
    # Total number of files scanned
    # Total number of duplicate files found
    # Consider below command line options for the gives script
    # DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
    # - DuplicateFileRemoval.py
    # Name of python automation script
    # - E:/Data/Demo
    # Absolute path of directory which may contains duplicate files
    # - 50
    # Time interval of script in minutes
    # - marvellousinfosystem@gmail.com
    # Mail ID of the receiver
    # Note :
    # For every separate task write separate function.
    # Write all user defined functions in one user defined module.
    # Use proper validation techniques.
    # Provide Help and usage option for script.
    # Create one Readme file which contains description of our script, details of command line options.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 22>python Assignment22_1.py Demo 5 ajay.mahamuni@gmail.com
    # Email sent successfully to :  ajay.mahamuni@gmail.com
    # Total files scanned : 59

    # Duplicate deleted files : 28

    # Process start time : 2025-06-27 21:06:43.538676

    # Process end time : 2025-06-27 21:06:43.603995

    # Total time taken by the process to complete the task : 0:00:00.065319

    # Log file created with name :  D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 22\Marvellous\MarvellousLog27062025-2106.log

    # Hello There,
    # This email contains summary of Automation process for deleting ducplicate files of a particular directory.
    # Below are the details of summary and log file is attached for your reference.
    # Total files scanned : 10255
    # Duplicate deleted files : 10224
    # Process start time : 2025-06-27 21:11:50.130573
    # Process end time : 2025-06-27 21:11:55.856923
    # Total time taken by the process to complete the task : 0:00:05.726350