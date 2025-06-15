#Assignment 17 - Problem 4 - Python automation implementation

import schedule  # type: ignore
import time
import datetime

def Display():
    timeOfDay = datetime.datetime.now().strftime("%H")

    # print("Time of day : ", timeOfDay)

    if timeOfDay == "09":
        print("Namaskar...", datetime.datetime.now())

def main():
    schedule.every(1).hour.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 4. Create a task that runs once every day at 9:00 AM and prints “Namskar...”