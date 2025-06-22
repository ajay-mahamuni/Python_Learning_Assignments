#Assignment 21 - Problem 1 - Python automation of processes

import psutil
import os
import datetime
import time # type: ignore
import schedule
import sys

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

def ProcessScan():

    
    cnt = 0

    try :
        for proc in psutil.process_iter():
            info = proc.as_dict(attrs=["name","pid","username"])
            info["vms"] = proc.memory_info().vms / (1024 * 1024)
            cnt = cnt + 1
            print(info)
            
        print("Total number of processes : ",cnt)

        

    except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
        pass #dont handle exception
    

def main():    
    ProcessScan()

    

if __name__ == "__main__":
    main()

    # 1.Design automation script which display information of running processes as its name, PID,Username.
    # Usage : ProcInfo.py

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 21>python Assignment21_1.py
    # {'pid': 0, 'username': 'NT AUTHORITY\\SYSTEM', 'name': 'System Idle Process', 'vms': 0.05859375}
    # {'pid': 4, 'username': 'NT AUTHORITY\\SYSTEM', 'name': 'System', 'vms': 0.0546875}
    # {'pid': 272, 'username': None, 'name': 'Registry', 'vms': 15.35546875}
    # {'pid': 744, 'username': None, 'name': 'svchost.exe', 'vms': 3.515625}
    # {'pid': 772, 'username': None, 'name': 'smss.exe', 'vms': 1.1484375}
    # {'pid': 1068, 'username': None, 'name': 'svchost.exe', 'vms': 1.578125}
    # {'pid': 1096, 'username': None, 'name': 'csrss.exe', 'vms': 2.7109375}
    # {'pid': 1200, 'username': None, 'name': 'wininit.exe', 'vms': 1.55859375}
    # {'pid': 1208, 'username': None, 'name': 'csrss.exe', 'vms': 4.83203125}
    # {'pid': 1272, 'username': None, 'name': 'services.exe', 'vms': 7.71875}
    # {'pid': 1280, 'username': None, 'name': 'lsass.exe', 'vms': 24.76953125}
    # {'pid': 1316, 'username': None, 'name': 'svchost.exe', 'vms': 5.3984375}
    # {'pid': 1332, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'UserOOBEBroker.exe', 'vms': 2.2421875}
    # {'pid': 1412, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 2.25390625}
    # {'pid': 1428, 'username': None, 'name': 'svchost.exe', 'vms': 52.84375}
    # {'pid': 1460, 'username': None, 'name': 'fontdrvhost.exe', 'vms': 2.3359375}
    # {'pid': 1468, 'username': None, 'name': 'WUDFHost.exe', 'vms': 23.8203125}
    # {'pid': 1568, 'username': None, 'name': 'svchost.exe', 'vms': 43.16796875}
    # {'pid': 1628, 'username': None, 'name': 'svchost.exe', 'vms': 3.75390625}
    # {'pid': 1696, 'username': None, 'name': 'winlogon.exe', 'vms': 3.06640625}
    # {'pid': 1748, 'username': None, 'name': 'WUDFHost.exe', 'vms': 1.51953125}
    # {'pid': 1756, 'username': None, 'name': 'fontdrvhost.exe', 'vms': 6.2734375}
    # {'pid': 1836, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 2.33203125}
    # {'pid': 1876, 'username': None, 'name': 'dwm.exe', 'vms': 471.8984375}
    # {'pid': 1944, 'username': None, 'name': 'svchost.exe', 'vms': 11.953125}
    # {'pid': 1956, 'username': None, 'name': 'svchost.exe', 'vms': 2.640625}
    # {'pid': 1964, 'username': None, 'name': 'svchost.exe', 'vms': 5.86328125}
    # {'pid': 1976, 'username': None, 'name': 'svchost.exe', 'vms': 4.19140625}
    # {'pid': 2060, 'username': None, 'name': 'svchost.exe', 'vms': 3.4921875}
    # {'pid': 2068, 'username': None, 'name': 'svchost.exe', 'vms': 2.76953125}
    # {'pid': 2180, 'username': None, 'name': 'IntelCpHDCPSvc.exe', 'vms': 1.6484375}
    # {'pid': 2212, 'username': None, 'name': 'svchost.exe', 'vms': 7.23828125}
    # {'pid': 2220, 'username': None, 'name': 'svchost.exe', 'vms': 4.15234375}
    # {'pid': 2308, 'username': None, 'name': 'svchost.exe', 'vms': 1.78125}
    # {'pid': 2332, 'username': None, 'name': 'svchost.exe', 'vms': 1.60546875}
    # {'pid': 2352, 'username': None, 'name': 'Code.exe', 'vms': 41.6640625}
    # {'pid': 2368, 'username': None, 'name': 'svchost.exe', 'vms': 17.82421875}
    # {'pid': 2376, 'username': None, 'name': 'svchost.exe', 'vms': 2.37890625}
    # {'pid': 2384, 'username': None, 'name': 'svchost.exe', 'vms': 2.9453125}
    # {'pid': 2440, 'username': None, 'name': 'svchost.exe', 'vms': 9.234375}
    # {'pid': 2448, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.2890625}
    # {'pid': 2564, 'username': None, 'name': 'svchost.exe', 'vms': 2.69140625}
    # {'pid': 2624, 'username': None, 'name': 'conhost.exe', 'vms': 6.94140625}
    # {'pid': 2648, 'username': None, 'name': 'svchost.exe', 'vms': 7.44140625}
    # {'pid': 2736, 'username': None, 'name': 'svchost.exe', 'vms': 3.9609375}
    # {'pid': 2764, 'username': None, 'name': 'svchost.exe', 'vms': 107.0234375}
    # {'pid': 2780, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 273.90234375}
    # {'pid': 2788, 'username': None, 'name': 'svchost.exe', 'vms': 10.34375}
    # {'pid': 2852, 'username': None, 'name': 'svchost.exe', 'vms': 4.52734375}
    # {'pid': 3080, 'username': None, 'name': 'svchost.exe', 'vms': 3.08984375}
    # {'pid': 3144, 'username': None, 'name': 'NVDisplay.Container.exe', 'vms': 25.86328125}
    # {'pid': 3264, 'username': None, 'name': 'node.exe', 'vms': 93.26171875}
    # {'pid': 3288, 'username': None, 'name': 'svchost.exe', 'vms': 21.72265625}
    # {'pid': 3328, 'username': None, 'name': 'svchost.exe', 'vms': 1.49609375}
    # {'pid': 3336, 'username': None, 'name': 'svchost.exe', 'vms': 3.421875}
    # {'pid': 3344, 'username': None, 'name': 'svchost.exe', 'vms': 2.41015625}
    # {'pid': 3424, 'username': None, 'name': 'svchost.exe', 'vms': 3.3515625}
    # {'pid': 3456, 'username': None, 'name': 'svchost.exe', 'vms': 4.36328125}
    # {'pid': 3468, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 121.4140625}
    # {'pid': 3504, 'username': None, 'name': 'MemCompression', 'vms': 8.0}
    # {'pid': 3572, 'username': None, 'name': 'svchost.exe', 'vms': 2.65234375}
    # {'pid': 3612, 'username': None, 'name': 'igfxCUIServiceN.exe', 'vms': 2.70703125}
    # {'pid': 3648, 'username': None, 'name': 'svchost.exe', 'vms': 3.12890625}
    # {'pid': 3656, 'username': None, 'name': 'svchost.exe', 'vms': 2.69140625}
    # {'pid': 3692, 'username': None, 'name': 'AggregatorHost.exe', 'vms': 6.93359375}
    # {'pid': 3784, 'username': None, 'name': 'svchost.exe', 'vms': 5.4765625}
    # {'pid': 3816, 'username': None, 'name': 'svchost.exe', 'vms': 1.64453125}
    # {'pid': 3824, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 307.0234375}
    # {'pid': 3892, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 1001.9609375}
    # {'pid': 3900, 'username': None, 'name': 'svchost.exe', 'vms': 2.88671875}
    # {'pid': 3908, 'username': None, 'name': 'PulseSecureService.exe', 'vms': 23.59765625}
    # {'pid': 3944, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 157.65625}
    # {'pid': 3952, 'username': None, 'name': 'svchost.exe', 'vms': 2.45703125}
    # {'pid': 3996, 'username': None, 'name': 'svchost.exe', 'vms': 8.58984375}
    # {'pid': 4024, 'username': None, 'name': 'svchost.exe', 'vms': 12.97265625}
    # {'pid': 4052, 'username': None, 'name': 'svchost.exe', 'vms': 3.25}
    # {'pid': 4092, 'username': None, 'name': 'svchost.exe', 'vms': 110.90234375}
    # {'pid': 4228, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 17.28515625}
    # {'pid': 4232, 'username': None, 'name': 'svchost.exe', 'vms': 17.99609375}
    # {'pid': 4328, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 10.40234375}
    # {'pid': 4428, 'username': None, 'name': 'NVDisplay.Container.exe', 'vms': 55.890625}
    # {'pid': 4476, 'username': None, 'name': 'WUDFHost.exe', 'vms': 2.0390625}
    # {'pid': 4720, 'username': None, 'name': 'svchost.exe', 'vms': 1.98046875}
    # {'pid': 4864, 'username': None, 'name': 'WmiPrvSE.exe', 'vms': 66.76171875}
    # {'pid': 4888, 'username': None, 'name': 'WmiPrvSE.exe', 'vms': 37.01953125}
    # {'pid': 4948, 'username': None, 'name': 'svchost.exe', 'vms': 1.875}
    # {'pid': 5016, 'username': None, 'name': 'dasHost.exe', 'vms': 9.4375}
    # {'pid': 5108, 'username': None, 'name': 'WUDFHost.exe', 'vms': 28.9140625}
    # {'pid': 5160, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Notepad.exe', 'vms': 66.86328125}
    # {'pid': 5300, 'username': None, 'name': 'svchost.exe', 'vms': 2.5625}
    # {'pid': 5360, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SSScheduler.exe', 'vms': 2.2109375}
    # {'pid': 5412, 'username': None, 'name': 'svchost.exe', 'vms': 22.79296875}
    # {'pid': 5436, 'username': None, 'name': 'jhi_service.exe', 'vms': 1.375}
    # {'pid': 5452, 'username': None, 'name': 'IntelAudioService.exe', 'vms': 39.51171875}
    # {'pid': 5476, 'username': None, 'name': 'svchost.exe', 'vms': 2.87890625}
    # {'pid': 5500, 'username': None, 'name': 'OneApp.IGCC.WinService.exe', 'vms': 35.00390625}
    # {'pid': 5552, 'username': None, 'name': 'WMIRegistrationService.exe', 'vms': 2.953125}
    # {'pid': 5624, 'username': None, 'name': 'RtkAudUService64.exe', 'vms': 5.39453125}
    # {'pid': 5656, 'username': None, 'name': 'svchost.exe', 'vms': 3.25390625}
    # {'pid': 5780, 'username': None, 'name': 'spoolsv.exe', 'vms': 7.63671875}
    # {'pid': 5808, 'username': None, 'name': 'svchost.exe', 'vms': 3.5625}
    # {'pid': 5892, 'username': None, 'name': 'svchost.exe', 'vms': 2.12109375}
    # {'pid': 5916, 'username': None, 'name': 'svchost.exe', 'vms': 2.7109375}
    # {'pid': 5936, 'username': None, 'name': 'WavesSysSvc64.exe', 'vms': 19.92578125}
    # {'pid': 5952, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 543.27734375}
    # {'pid': 6068, 'username': None, 'name': 'svchost.exe', 'vms': 54.23046875}
    # {'pid': 6076, 'username': None, 'name': 'svchost.exe', 'vms': 6.95703125}
    # {'pid': 6096, 'username': None, 'name': 'svchost.exe', 'vms': 4.49609375}
    # {'pid': 6104, 'username': None, 'name': 'svchost.exe', 'vms': 30.5625}
    # {'pid': 6112, 'username': None, 'name': 'DPMService.exe', 'vms': 21.17578125}
    # {'pid': 6140, 'username': None, 'name': 'svchost.exe', 'vms': 6.1328125}
    # {'pid': 6160, 'username': None, 'name': 'TeamViewer_Service.exe', 'vms': 16.9921875}
    # {'pid': 6168, 'username': None, 'name': 'mysqld.exe', 'vms': 33.171875}
    # {'pid': 6176, 'username': None, 'name': 'esif_uf.exe', 'vms': 2.1328125}
    # {'pid': 6184, 'username': None, 'name': 'WavesAudioService.exe', 'vms': 13.75390625}
    # {'pid': 6192, 'username': None, 'name': 'nvWmi64.exe', 'vms': 3.765625}
    # {'pid': 6204, 'username': None, 'name': 'svchost.exe', 'vms': 3.125}
    # {'pid': 6224, 'username': None, 'name': 'svchost.exe', 'vms': 6.12109375}
    # {'pid': 6244, 'username': None, 'name': 'sqlwriter.exe', 'vms': 2.27734375}
    # {'pid': 6256, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'powershell.exe', 'vms': 56.15234375}
    # {'pid': 6268, 'username': None, 'name': 'TbtP2pShortcutService.exe', 'vms': 1.6015625}
    # {'pid': 6312, 'username': None, 'name': 'svchost.exe', 'vms': 1.9609375}
    # {'pid': 6328, 'username': None, 'name': 'svchost.exe', 'vms': 3.96875}
    # {'pid': 6348, 'username': None, 'name': 'svchost.exe', 'vms': 6.3203125}
    # {'pid': 6372, 'username': None, 'name': 'Code.exe', 'vms': 50.1953125}
    # {'pid': 6420, 'username': None, 'name': 'svchost.exe', 'vms': 3.34375}
    # {'pid': 6628, 'username': None, 'name': 'Postman.exe', 'vms': 197.359375}
    # {'pid': 6636, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.3515625}
    # {'pid': 6652, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 44.39453125}
    # {'pid': 6916, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'CalculatorApp.exe', 'vms': 51.61328125}
    # {'pid': 7104, 'username': None, 'name': 'DPMCrashHandler.exe', 'vms': 1.2421875}
    # {'pid': 7268, 'username': None, 'name': 'mysqld.exe', 'vms': 586.41015625}
    # {'pid': 7488, 'username': None, 'name': 'conhost.exe', 'vms': 1.5546875}
    # {'pid': 7712, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 2.30859375}
    # {'pid': 7736, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Code.exe', 'vms': 25.40234375}
    # {'pid': 7836, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 58.97265625}
    # {'pid': 7860, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 7.48828125}
    # {'pid': 7968, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 2.18359375}
    # {'pid': 8044, 'username': None, 'name': 'PulseSecureService.exe', 'vms': 360.9140625}
    # {'pid': 8136, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 2.6640625}
    # {'pid': 8828, 'username': None, 'name': 'svchost.exe', 'vms': 231.7421875}
    # {'pid': 8912, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 12.4921875}
    # {'pid': 9076, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 2.5}
    # {'pid': 9408, 'username': None, 'name': 'svchost.exe', 'vms': 3.42578125}
    # {'pid': 9448, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'sihost.exe', 'vms': 19.9296875}
    # {'pid': 9616, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 27.17578125}
    # {'pid': 9676, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.2265625}
    # {'pid': 9696, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.27734375}
    # {'pid': 9732, 'username': None, 'name': 'PresentationFontCache.exe', 'vms': 29.671875}
    # {'pid': 9792, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'dptf_helper.exe', 'vms': 1.6796875}
    # {'pid': 9924, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'DPM.exe', 'vms': 88.9140625}
    # {'pid': 9936, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 224.57421875}
    # {'pid': 9952, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 13.859375}
    # {'pid': 10020, 'username': None, 'name': 'nvWmi64.exe', 'vms': 7.12890625}
    # {'pid': 10060, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'taskhostw.exe', 'vms': 15.7421875}
    # {'pid': 10148, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'DPMCrashHandler.exe', 'vms': 1.4921875}
    # {'pid': 10172, 'username': None, 'name': 'svchost.exe', 'vms': 15.34765625}
    # {'pid': 10300, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 71.62109375}
    # {'pid': 10312, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'PhoneExperienceHost.exe', 'vms': 159.99609375}
    # {'pid': 10316, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'EXCEL.EXE', 'vms': 573.5078125}
    # {'pid': 10376, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.25}
    # {'pid': 10508, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'igfxEMN.exe', 'vms': 4.67578125}
    # {'pid': 10528, 'username': None, 'name': 'svchost.exe', 'vms': 5.375}
    # {'pid': 10688, 'username': None, 'name': 'svchost.exe', 'vms': 7.0234375}
    # {'pid': 10696, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'explorer.exe', 'vms': 1182.76171875}
    # {'pid': 10728, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 7.453125}
    # {'pid': 10780, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.21484375}
    # {'pid': 10992, 'username': None, 'name': 'unsecapp.exe', 'vms': 2.3515625}
    # {'pid': 11060, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'WavesSvc64.exe', 'vms': 225.3125}
    # {'pid': 11172, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 416.1484375}
    # {'pid': 11300, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 2.6171875}
    # {'pid': 11724, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 47.4140625}
    # {'pid': 11740, 'username': None, 'name': 'RtkAudUService64.exe', 'vms': 4.5234375}
    # {'pid': 11788, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'StartMenuExperienceHost.exe', 'vms': 131.82421875}
    # {'pid': 11828, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SearchHost.exe', 'vms': 293.41015625}
    # {'pid': 11848, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 14.45703125}
    # {'pid': 11980, 'username': None, 'name': 'svchost.exe', 'vms': 15.0390625}
    # {'pid': 12052, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 5.359375}
    # {'pid': 12116, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 21.86328125}
    # {'pid': 12192, 'username': None, 'name': 'svchost.exe', 'vms': 3.8125}
    # {'pid': 12236, 'username': None, 'name': 'McCHSvc.exe', 'vms': 3.3671875}
    # {'pid': 12400, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'dllhost.exe', 'vms': 8.8984375}
    # {'pid': 12408, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Widgets.exe', 'vms': 30.19921875}
    # {'pid': 12452, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 9.671875}
    # {'pid': 12464, 'username': None, 'name': 'WmiApSrv.exe', 'vms': 2.734375}
    # {'pid': 12488, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 3.859375}
    # {'pid': 12496, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 30.81640625}
    # {'pid': 12620, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 18.88671875}
    # {'pid': 12724, 'username': None, 'name': 'svchost.exe', 'vms': 1.46875}
    # {'pid': 12748, 'username': None, 'name': 'WmiPrvSE.exe', 'vms': 6.7109375}
    # {'pid': 12856, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.08984375}
    # {'pid': 13240, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 14.0703125}
    # {'pid': 13244, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ms-teams.exe', 'vms': 185.5859375}
    # {'pid': 13404, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ShellExperienceHost.exe', 'vms': 94.03125}
    # {'pid': 13424, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 16.34375}
    # {'pid': 13608, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 1.66796875}
    # {'pid': 13620, 'username': None, 'name': 'Code.exe', 'vms': 19.10546875}
    # {'pid': 14284, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ctfmon.exe', 'vms': 41.0390625}
    # {'pid': 14476, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 19.0390625}
    # {'pid': 14552, 'username': None, 'name': 'svchost.exe', 'vms': 21.30859375}
    # {'pid': 14680, 'username': None, 'name': 'svchost.exe', 'vms': 38.74609375}
    # {'pid': 14752, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'TextInputHost.exe', 'vms': 47.921875}
    # {'pid': 14764, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'unsecapp.exe', 'vms': 2.10546875}
    # {'pid': 14816, 'username': None, 'name': 'svchost.exe', 'vms': 37.06640625}
    # {'pid': 15160, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SecurityHealthSystray.exe', 'vms': 2.30078125}
    # {'pid': 15180, 'username': None, 'name': 'SecurityHealthService.exe', 'vms': 9.70703125}
    # {'pid': 15240, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RtkAudUService64.exe', 'vms': 5.34375}
    # {'pid': 15292, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'cmd.exe', 'vms': 1.859375}
    # {'pid': 15556, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 21.81640625}
    # {'pid': 15596, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Video.UI.exe', 'vms': 35.80859375}
    # {'pid': 15772, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.28515625}
    # {'pid': 15956, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'conhost.exe', 'vms': 1.4765625}
    # {'pid': 16128, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ApplicationFrameHost.exe', 'vms': 77.9609375}
    # {'pid': 16200, 'username': None, 'name': 'armsvc.exe', 'vms': 1.73046875}
    # {'pid': 16292, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 8.02734375}
    # {'pid': 16300, 'username': None, 'name': 'svchost.exe', 'vms': 1.83203125}
    # {'pid': 16548, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'notepad++.exe', 'vms': 36.85546875}
    # {'pid': 16564, 'username': None, 'name': 'Code.exe', 'vms': 81.07421875}
    # {'pid': 16588, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 4.8125}
    # {'pid': 16640, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 7.28125}
    # {'pid': 16776, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 141.5}
    # {'pid': 16896, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'AcrobatNotificationClient.exe', 'vms': 29.40234375}
    # {'pid': 17452, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.35546875}
    # {'pid': 17712, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'CrossDeviceService.exe', 'vms': 24.80859375}
    # {'pid': 17732, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 217.3984375}
    # {'pid': 17804, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'conhost.exe', 'vms': 1.6953125}
    # {'pid': 17888, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'WidgetService.exe', 'vms': 5.578125}
    # {'pid': 17988, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 2.66796875}
    # {'pid': 18096, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'dllhost.exe', 'vms': 17.890625}
    # {'pid': 18200, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Code.exe', 'vms': 378.6640625}
    # {'pid': 18260, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SDXHelper.exe', 'vms': 23.78515625}
    # {'pid': 18576, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'taskhostw.exe', 'vms': 19.67578125}
    # {'pid': 18864, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Code.exe', 'vms': 14.1875}
    # {'pid': 19004, 'username': None, 'name': 'svchost.exe', 'vms': 2.95703125}
    # {'pid': 19192, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'BackgroundTransferHost.exe', 'vms': 2.92578125}
    # {'pid': 19428, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'powershell.exe', 'vms': 61.26171875}
    # {'pid': 19816, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.3203125}
    # {'pid': 19864, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 26.39453125}
    # {'pid': 19904, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'CalculatorApp.exe', 'vms': 51.95703125}
    # {'pid': 20212, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 197.9375}
    # {'pid': 20268, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 434.93359375}
    # {'pid': 20276, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'cmd.exe', 'vms': 5.40625}
    # {'pid': 20400, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Pulse.exe', 'vms': 32.88671875}
    # {'pid': 20488, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.2109375}
    # {'pid': 20548, 'username': None, 'name': 'svchost.exe', 'vms': 3.87109375}
    # {'pid': 20756, 'username': None, 'name': 'Code.exe', 'vms': 34.4140625}
    # {'pid': 20820, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 519.99609375}
    # {'pid': 20996, 'username': None, 'name': 'svchost.exe', 'vms': 3.80859375}
    # {'pid': 21100, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.29296875}
    # {'pid': 21200, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'svchost.exe', 'vms': 6.15234375}
    # {'pid': 21380, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 56.57421875}
    # {'pid': 21476, 'username': None, 'name': 'OfficeClickToRun.exe', 'vms': 54.3046875}
    # {'pid': 21964, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 15.39453125}
    # {'pid': 22104, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 365.34765625}
    # {'pid': 22180, 'username': None, 'name': 'Microsoft.Management.Services.IntuneWindowsAgent.exe', 'vms': 45.23046875}
    # {'pid': 22344, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'WindowsPackageManagerServer.exe', 'vms': 17.40625}
    # {'pid': 22396, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 8.23828125}
    # {'pid': 22452, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SnagitEditor.exe', 'vms': 294.69921875}
    # {'pid': 22508, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.328125}
    # {'pid': 22580, 'username': None, 'name': 'svchost.exe', 'vms': 2.55078125}
    # {'pid': 23008, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 21.89453125}
    # {'pid': 23220, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 5.12890625}
    # {'pid': 23480, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Code.exe', 'vms': 247.6015625}
    # {'pid': 23880, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.28125}
    # {'pid': 23964, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'CalculatorApp.exe', 'vms': 51.640625}
    # {'pid': 24240, 'username': None, 'name': 'svchost.exe', 'vms': 2.54296875}
    # {'pid': 24484, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.27734375}
    # {'pid': 24628, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SnagPriv.exe', 'vms': 2.3671875}
    # {'pid': 25020, 'username': None, 'name': 'unsecapp.exe', 'vms': 2.34765625}
    # {'pid': 25096, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'wa_3rd_party_host_32.exe', 'vms': 44.19140625}
    # {'pid': 25104, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'conhost.exe', 'vms': 1.140625}
    # {'pid': 25176, 'username': None, 'name': 'svchost.exe', 'vms': 2.36328125}
    # {'pid': 25204, 'username': None, 'name': 'wa_3rd_party_host_32.exe', 'vms': 90.0234375}
    # {'pid': 25212, 'username': None, 'name': 'conhost.exe', 'vms': 1.015625}
    # {'pid': 25424, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'PulseSetupClient.exe', 'vms': 4.09765625}
    # {'pid': 25476, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'splwow64.exe', 'vms': 6.734375}
    # {'pid': 25492, 'username': None, 'name': 'svchost.exe', 'vms': 7.11328125}
    # {'pid': 25672, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 54.62890625}
    # {'pid': 26928, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'python3.13.exe', 'vms': 11.3203125}
    # {'pid': 26964, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 187.57421875}
    # {'pid': 27072, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SearchProtocolHost.exe', 'vms': 13.578125}
    # {'pid': 27276, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 3.02734375}
    # {'pid': 27488, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 277.36328125}
    # {'pid': 27500, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.1796875}
    # {'pid': 27712, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 21.05859375}
    # {'pid': 27776, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 236.6171875}
    # {'pid': 27792, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 8.39453125}
    # {'pid': 27836, 'username': None, 'name': 'Postman.exe', 'vms': 20.21875}
    # {'pid': 28320, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 5.55078125}
    # {'pid': 28400, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'OpenConsole.exe', 'vms': 3.3359375}
    # {'pid': 28520, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'dllhost.exe', 'vms': 1.8359375}
    # {'pid': 28540, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.21484375}
    # {'pid': 28808, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.29296875}
    # {'pid': 28932, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 89.99609375}
    # {'pid': 29088, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'crashpad_handler.exe', 'vms': 1.45703125}
    # {'pid': 29396, 'username': None, 'name': 'svchost.exe', 'vms': 2.62109375}
    # {'pid': 29836, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.26953125}
    # {'pid': 30116, 'username': None, 'name': 'servicehost.exe', 'vms': 35.3125}
    # {'pid': 30180, 'username': None, 'name': 'NisSrv.exe', 'vms': 4.8125}
    # {'pid': 30192, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'dllhost.exe', 'vms': 2.7890625}
    # {'pid': 30456, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'OUTLOOK.EXE', 'vms': 252.91796875}
    # {'pid': 30572, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.3125}
    # {'pid': 31092, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ms-teamsupdate.exe', 'vms': 5.17578125}
    # {'pid': 31152, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 146.2109375}
    # {'pid': 31240, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.19921875}
    # {'pid': 31284, 'username': None, 'name': 'svchost.exe', 'vms': 2.09375}
    # {'pid': 31356, 'username': None, 'name': 'Postman.exe', 'vms': 362.51171875}
    # {'pid': 31812, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 17.1484375}
    # {'pid': 32528, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 294.171875}
    # {'pid': 32644, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'CalculatorApp.exe', 'vms': 52.0546875}
    # {'pid': 32820, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 1458.57421875}
    # {'pid': 32828, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Postman.exe', 'vms': 12.515625}
    # {'pid': 32904, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 26.25}
    # {'pid': 33040, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Postman.exe', 'vms': 332.9296875}
    # {'pid': 33168, 'username': None, 'name': 'SearchProtocolHost.exe', 'vms': 2.82421875}
    # {'pid': 33412, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 171.0625}
    # {'pid': 33500, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 310.47265625}
    # {'pid': 33624, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Code.exe', 'vms': 645.6640625}
    # {'pid': 33716, 'username': None, 'name': 'svchost.exe', 'vms': 1.37109375}
    # {'pid': 33828, 'username': None, 'name': 'audiodg.exe', 'vms': 8.71484375}
    # {'pid': 34892, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'WWAHost.exe', 'vms': 60.671875}
    # {'pid': 34996, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 250.76953125}
    # {'pid': 35172, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'AppVShNotify.exe', 'vms': 1.8515625}
    # {'pid': 35284, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'conhost.exe', 'vms': 1.703125}
    # {'pid': 35380, 'username': None, 'name': 'MoUsoCoreWorker.exe', 'vms': 74.76953125}
    # {'pid': 36644, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'SnagitCapture.exe', 'vms': 266.359375}
    # {'pid': 36664, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'crashpad_handler.exe', 'vms': 1.46484375}
    # {'pid': 36668, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 68.74609375}
    # {'pid': 36724, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.1875}
    # {'pid': 36792, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.234375}
    # {'pid': 37280, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 22.13671875}
    # {'pid': 37612, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 15.3515625}
    # {'pid': 37672, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.38671875}
    # {'pid': 37848, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 24.66796875}
    # {'pid': 38048, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 42.640625}
    # {'pid': 38088, 'username': None, 'name': 'Code.exe', 'vms': 109.10546875}
    # {'pid': 38268, 'username': None, 'name': 'svchost.exe', 'vms': 1.99609375}
    # {'pid': 38272, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'HxTsr.exe', 'vms': 11.63671875}
    # {'pid': 38276, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 22.13671875}
    # {'pid': 38480, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.30078125}
    # {'pid': 38884, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.33984375}
    # {'pid': 38920, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Microsoft.SharePoint.exe', 'vms': 413.8203125}
    # {'pid': 38940, 'username': None, 'name': 'MsMpEng.exe', 'vms': 401.8984375}
    # {'pid': 39048, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 10.66796875}
    # {'pid': 39060, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Postman.exe', 'vms': 11.51171875}
    # {'pid': 39152, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 3.015625}
    # {'pid': 39324, 'username': None, 'name': 'MpDefenderCoreService.exe', 'vms': 15.46875}
    # {'pid': 39632, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'WindowsTerminal.exe', 'vms': 103.671875}
    # {'pid': 39940, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.390625}
    # {'pid': 40164, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 24.21875}
    # {'pid': 40400, 'username': None, 'name': 'svchost.exe', 'vms': 3.37109375}
    # {'pid': 40820, 'username': None, 'name': 'svchost.exe', 'vms': 5.8203125}
    # {'pid': 41044, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 24.48046875}
    # {'pid': 41156, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 990.78515625}
    # {'pid': 41548, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'LockApp.exe', 'vms': 41.44140625}
    # {'pid': 41616, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ms-teams.exe', 'vms': 86.3515625}
    # {'pid': 41740, 'username': None, 'name': 'SearchIndexer.exe', 'vms': 57.9765625}
    # {'pid': 42024, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ShellHost.exe', 'vms': 33.56640625}
    # {'pid': 42164, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 234.609375}
    # {'pid': 42196, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.3359375}
    # {'pid': 42292, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 72.7265625}
    # {'pid': 42556, 'username': None, 'name': 'svchost.exe', 'vms': 1.83984375}
    # {'pid': 43520, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 29.49609375}
    # {'pid': 43592, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'conhost.exe', 'vms': 1.484375}
    # {'pid': 43908, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 2.53515625}
    # {'pid': 44216, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 28.27734375}
    # {'pid': 44528, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 179.16015625}
    # {'pid': 44544, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 44.703125}
    # {'pid': 44820, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 11.390625}
    # {'pid': 44892, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 41.9765625}
    # {'pid': 45732, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 62.62109375}
    # {'pid': 45792, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'uihost.exe', 'vms': 16.80859375}
    # {'pid': 45932, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 24.3671875}
    # {'pid': 46252, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'python3.13.exe', 'vms': 12.40625}
    # {'pid': 46692, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 25.93359375}
    # {'pid': 46876, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 22.23828125}
    # {'pid': 46980, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'backgroundTaskHost.exe', 'vms': 18.07421875}
    # {'pid': 47008, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 7.48828125}
    # {'pid': 47296, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'browserhost.exe', 'vms': 8.0859375}
    # {'pid': 47452, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'Spotify.exe', 'vms': 25.5859375}
    # {'pid': 47516, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 2.26953125}
    # {'pid': 47892, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 90.9296875}
    # {'pid': 48016, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 159.421875}
    # {'pid': 48056, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'RuntimeBroker.exe', 'vms': 3.49609375}
    # {'pid': 48080, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'ai.exe', 'vms': 22.73828125}
    # {'pid': 48112, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'msedgewebview2.exe', 'vms': 12.01171875}
    # {'pid': 48140, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 25.26953125}
    # {'pid': 48264, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 176.75}
    # {'pid': 48284, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 99.06640625}
    # {'pid': 48368, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 21.8203125}
    # {'pid': 48684, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 21.05078125}
    # {'pid': 48888, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 26.06640625}
    # {'pid': 49040, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 60.8359375}
    # {'pid': 49060, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 37.94140625}
    # {'pid': 49260, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 50.74609375}
    # {'pid': 49924, 'username': 'DESKTOP-7R3FVDN\\DELL', 'name': 'chrome.exe', 'vms': 600.50390625}
    # {'pid': 50692, 'username': None, 'name': 'svchost.exe', 'vms': 49.51953125}
    # {'pid': 50700, 'username': None, 'name': 'SearchFilterHost.exe', 'vms': 1.984375}
    # Total number of processes :  398