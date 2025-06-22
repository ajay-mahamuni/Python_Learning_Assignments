#Assignment 21 - Problem 4 - Python automation of processes

import psutil
import os
import datetime
import time # type: ignore
import schedule
import sys
import EmailModule # type: ignore

def CreateLog(folderName):
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    dateFormat = datetime.datetime.now()
    dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%H%M").replace(":","")

    fileName = "MarvellousLog%s.log" %(dateFormat)
    fileName = fileName.replace(":","")
    fileName = fileName.replace(" ","_")

    fileName = os.path.join(folderName,fileName)    

    fObj = open(fileName,"w")

    border = "-"*80 + "\n"
    fObj.write(border)
    fObj.write("Process Monitoring Logs \n")
    fObj.write(border)

    logData = ProcessScan()
    
    for values in logData:
        fObj.write("%s \n" %values)
    fObj.write("Log file created at : "+ time.ctime()+"\n")
    fObj.write(border)

    fObj.close()

    print("Log file with name : ", fileName," is created.")

    fileName = os.path.abspath(fileName)

    EmailModule.send_email_using_gmail("Process Logs",fileName,"ajay.mahamuni@gmail.com")

    

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
    

def main():
    if len(sys.argv) > 1:
        CreateLog(sys.argv[1])

    

if __name__ == "__main__":
    main()

    # 4. Design automation script which accept directory name and mail id from user and create log
    # file in that directory which contains information of running processes as its name, PID,
    # Username. After creating log file send that log file to the specified mail.
    # Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
    # Demo is name of Directory.
    # marvellousinfosystem@gmail.com is the mail id.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 21>python Assignment21_4.py ProcessLog
    # Total number of processes :  384
    # Log file with name :  ProcessLog\MarvellousLog22062025-1440.log  is created.
    # Email sent successfully to :  ajay.mahamuni@gmail.com