#Assignment 17 - Problem 2 - Python automation implementation

import schedule  # type: ignore
import time
import datetime

def Display():
    print("Current date and time : ", datetime.datetime.now())

def main():
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 2. Schedule a task that displays the current date and time every minute using the
    # datetime module.

    
    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17>python Assignment17_2.py
    # Current date and time :  2025-06-13 20:16:13.156269
    # Current date and time :  2025-06-13 20:17:13.180920
    # Current date and time :  2025-06-13 20:18:13.201987
    # Current date and time :  2025-06-13 20:19:13.223858
    # Current date and time :  2025-06-13 20:20:13.245906
    # Current date and time :  2025-06-13 20:21:13.272279
    # Current date and time :  2025-06-13 20:22:13.295620
    # Current date and time :  2025-06-13 20:23:13.318119
    # Current date and time :  2025-06-13 20:24:13.343323
    # Current date and time :  2025-06-13 20:25:13.367767
    # Traceback (most recent call last):
    # File "D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17\Assignment17_2.py", line 18, in <module>
    #     main()
    #     ~~~~^^
    # File "D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17\Assignment17_2.py", line 15, in main
    #     time.sleep(1)
    #     ~~~~~~~~~~^^^
    # KeyboardInterrupt
    # ^C