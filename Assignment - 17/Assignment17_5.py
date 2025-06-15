#Assignment 17 - Problem 5 - Python automation implementation

import schedule  # type: ignore
import time
import datetime
import os

def WriteFile():

    flag = os.path.exists("Marvellous.txt")

    if flag == True:
        aObj = open("Marvellous.txt","a")
        dateData = str(datetime.datetime.now()) + "\n"
        aObj.write(dateData)
        aObj.close()
    else:
        fObj = open("Marvellous.txt","w")
        dateData = str(datetime.datetime.now()) + "\n"
        fObj.write(dateData)
        fObj.close()

    
def main():
    schedule.every(5).minutes.do(WriteFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 5. Schedule a job that runs every 5 minutes to write the current time to a file
    # Marvellous.txt.

    # 2025-06-13 22:41:09.592518
    # 2025-06-13 22:46:09.702974
    # 2025-06-13 22:51:09.830979
    # 2025-06-13 22:56:09.952041
    # 2025-06-13 23:01:10.073530
    # 2025-06-13 23:06:10.198616
    # 2025-06-13 23:11:10.314646
    # 2025-06-13 23:16:10.435747
    # 2025-06-13 23:21:10.556947
    # 2025-06-13 23:26:10.679359
