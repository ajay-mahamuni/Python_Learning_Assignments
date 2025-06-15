#Assignment 17 - Problem 6 - Python automation implementation

import schedule  # type: ignore
import time
import datetime

def Display():
    timeOfDay = datetime.datetime.now().strftime("%H")

    # print("Time of day : ", timeOfDay)

    if timeOfDay == "13":
        print("Lunch Time...", datetime.datetime.now())
    elif timeOfDay == "18":
        print("Wrap up work...", datetime.datetime.now())

def main():
    schedule.every(1).hour.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 6. Write a script that schedules multiple tasks: one to print "Lunch Time!" at 1 PM,
    # and another to print "Wrap up work" at 6 PM.