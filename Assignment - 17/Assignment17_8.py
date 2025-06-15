#Assignment 17 - Problem 8 - Python automation implementation

import schedule  # type: ignore
import time
import datetime

def CheckEmail():
    print("Checking email... ", datetime.datetime.now())

def main():
    schedule.every(10).seconds.do(CheckEmail)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 8. Write a script that simulates checking for email updates every 10 seconds. (Use a
    # print statement like “Checking mail...” instead of real email logic.)

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17>python Assignment17_8.py
    # Checking email...  2025-06-13 23:34:24.039218
    # Checking email...  2025-06-13 23:34:34.043589
    # Checking email...  2025-06-13 23:34:44.047992
    # Checking email...  2025-06-13 23:34:54.051896
    # Checking email...  2025-06-13 23:35:04.056150
    # Checking email...  2025-06-13 23:35:14.060974
    # Checking email...  2025-06-13 23:35:24.066236
    # Checking email...  2025-06-13 23:35:34.069730
    # Checking email...  2025-06-13 23:35:44.073134