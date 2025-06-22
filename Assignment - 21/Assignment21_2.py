#Assignment 21 - Problem 2 - Python automation of processes

import psutil
import os
import datetime
import time # type: ignore
import schedule
import sys

def CreateLog(folderName,processName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    dateFormat = datetime.datetime.now()
    dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%H%M").replace(":","")

    fileName = "MarvellousLog%s.log" %(dateFormat)
    fileName = fileName.replace(":","")
    fileName = fileName.replace(" ","_")

    fileName = os.path.join(folderName,fileName)    

    if os.path.exists(fileName):
        fObj = open(fileName,"a")
    else:
        fObj = open(fileName,"w")

    border = "-"*80 + "\n"
    fObj.write(border)
    fObj.write("Process Monitoring Logs \n")
    fObj.write(border)

    procDetails = ProcessDetails(processName)

    print("Process details :",procDetails)

    fObj.write("Process Id : \t %s \n" %procDetails.info["pid"])
    fObj.write("Status : \t%s \n" %procDetails.info["status"])
    # fObj.write("Process started at %s \n" %procDetails.info["started"])
    
    # fObj.write("%s \n" %procDetails)

    fObj.write("Log file created at : "+ time.ctime()+"\n")
    fObj.write(border)

    fObj.close()

    print("Log file with name : ", fileName," is created.")

def ProcessDetails(processName):
    for proc in psutil.process_iter(["name","status","pid"]):
        if proc.info["name"] == processName and proc.info["status"] == "running":
            return proc
            



def main():    
    CreateLog("ProcessLog",sys.argv[1])

if __name__ == "__main__":
    main()


def ProcessScan():

    listProcess = []
    cnt = 0

    try :
        for proc in psutil.process_iter():
            info = proc.as_dict(attrs=["name","pid","username"])
            info["vms"] = proc.memory_info().vms / (1024 * 1024)
            cnt = cnt + 1
            listProcess.append(info)

        print("Total number of processes : ",cnt)

        return listProcess

    except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
        pass #dont handle exception
    

    # 2.Design automation script which accept process name and display information of that process if it is running.
    # Usage : ProcInfo.py Notepad

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 21>python Assignment21_2.py Postman.exe
    # Process details : psutil.Process(pid=6628, name='Postman.exe', status='running', started='2025-06-11 15:24:02')
    # Log file with name :  ProcessLog\MarvellousLog22062025-0204.log  is created.