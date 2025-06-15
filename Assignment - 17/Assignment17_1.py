#Assignment 17 - Problem 1 - Python automation implementation

import schedule # type: ignore
import time
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    schedule.every(2).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


    # 1. Write a Python script that prints “Jay Ganesh...” every 2 seconds. Use the
    # schedule.every(2).seconds.do(...) function.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17>python Assignment17_1.py
    # Jay Ganesh... 2025-06-13 20:08:59.086592
    # Jay Ganesh... 2025-06-13 20:09:01.087839
    # Jay Ganesh... 2025-06-13 20:09:03.088895
    # Jay Ganesh... 2025-06-13 20:09:05.089804
    # Jay Ganesh... 2025-06-13 20:09:07.090846
    # Jay Ganesh... 2025-06-13 20:09:09.091874
    # Jay Ganesh... 2025-06-13 20:09:11.092944
    # Jay Ganesh... 2025-06-13 20:09:13.094794
    # Jay Ganesh... 2025-06-13 20:09:15.095694
    # Jay Ganesh... 2025-06-13 20:09:17.096933
    # Jay Ganesh... 2025-06-13 20:09:19.097774
    # Jay Ganesh... 2025-06-13 20:09:21.098831
    # Jay Ganesh... 2025-06-13 20:09:23.099655
    # Jay Ganesh... 2025-06-13 20:09:25.100691
    # Jay Ganesh... 2025-06-13 20:09:27.101424
    # Jay Ganesh... 2025-06-13 20:09:29.102856
    # Jay Ganesh... 2025-06-13 20:09:31.103677
    # Jay Ganesh... 2025-06-13 20:09:33.104564
    # Jay Ganesh... 2025-06-13 20:09:35.105285
    # Jay Ganesh... 2025-06-13 20:09:37.106380
    # Jay Ganesh... 2025-06-13 20:09:39.107923
    # Jay Ganesh... 2025-06-13 20:09:41.109380
    # Jay Ganesh... 2025-06-13 20:09:43.110873
    # Jay Ganesh... 2025-06-13 20:09:45.111633
    # Jay Ganesh... 2025-06-13 20:09:47.112682
    # Jay Ganesh... 2025-06-13 20:09:49.113704
    # Jay Ganesh... 2025-06-13 20:09:51.114711
    # Jay Ganesh... 2025-06-13 20:09:53.115574
    # Jay Ganesh... 2025-06-13 20:09:55.116514
    # Traceback (most recent call last):
    # File "D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17\Assignment17_1.py", line 18, in <module>
    #     main()
    #     ~~~~^^
    # File "D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 17\Assignment17_1.py", line 15, in main
    #     time.sleep(1)
    #     ~~~~~~~~~~^^^
    # KeyboardInterrupt
    # ^C