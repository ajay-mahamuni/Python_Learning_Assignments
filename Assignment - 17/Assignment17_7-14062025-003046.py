#Assignment 17 - Problem 6 - Python automation implementation

import schedule  # type: ignore
import time
import datetime
import os

def LogData(backUpFileName):

    fileName = "Log.log"

    if os.path.exists(fileName):
        aObj = open(fileName,"a")
        aObj.write("Backup file is created with name : ", backUpFileName,"\n")
        aObj.write("Backup file is created at time : ", str(datetime.datetime.now()),"\n")
        aObj.close()
    else:
        wObj = open(fileName,"w")
        wObj.write("Backup file is created with name : ", backUpFileName,"\n")
        wObj.write("Backup file is created at time : ", str(datetime.datetime.now()),"\n")
        wObj.close()
    
def BackUpFile():

    sourceFile = "Assignment17_7.py"

    fObj = open(sourceFile,"r")

    data = fObj.read()

    dateFormat = datetime.datetime.now()

    dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%X").replace(":","")

    destFile = "Assignment17_7-" + dateFormat + ".py"

    dObj = open(destFile,"w")

    dObj.write(data)

    fObj.close()

    dObj.close()

    LogData()

    LogData(destFile)


def main():
    schedule.every(1).hour.do(BackUpFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 7. Schedule a function that performs file backup every hour and writes a log entry
    # into backup_log.txt.