#Assignment 17 - Problem 3 - Python automation implementation

import schedule  # type: ignore
import time
import datetime

def Display():
    print("Do coding... ", datetime.datetime.now())

def main():
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 3. Write a program that schedules a function to print “Do Coding..!” every 30
    # minutes.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17>python Assignment17_3.py
    # Do coding...  2025-06-13 20:58:59.747880
    # Do coding...  2025-06-13 21:29:00.483170
    # Do coding...  2025-06-13 21:59:01.214302