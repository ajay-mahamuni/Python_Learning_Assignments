#Assignment 9 - Problem 1 - Multi threaded program with thread wait

import threading
import time


def ThreadLoop1():
    for i in range(1,6):
        print(i, end= " ")
        time.sleep(1)
    print(end = " \n")


# def ThreadLoop2():
#     for i in range(1,6):
#         print(i, end= " ")
#         time.sleep(1)
#     print(end = " \n")


# def ThreadLoop3():
#     for i in range(1,6):
#         print(i, end= " ")
#         time.sleep(1)
#     print(end = " \n")

def main():
    
    T1 = threading.Thread(target=ThreadLoop1)

    T2 = threading.Thread(target=ThreadLoop1)

    T3 = threading.Thread(target=ThreadLoop1)

    start_time_T1 = time.time()
    T1.start()

    start_time_T2 = time.time()
    T2.start()

    start_time_T3 = time.time()
    T3.start()

    T1.join()
    end_time_T1 = time.time()

    T2.join()
    end_time_T2 = time.time()

    T3.join()
    end_time_T3 = time.time()

    print("Time taken by Thread 1 : ",end_time_T1 - start_time_T1)

    print("Time taken by Thread 2 : ",end_time_T2 - start_time_T2)

    print("Time taken by Thread 3 : ",end_time_T3 - start_time_T3)
    
if __name__ == "__main__":
    main()

    # 1.Create a Python program that starts 3 threads, each printing numbers
    # from 1 to 5 with a delay of 1 second. Use threading.Thread.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 9>python Assignment9_1.py
    # 1 1 1 2 2 2 3 3 3 4 4 4 5 5 5


    # Time taken by Thread 1 :  5.0027265548706055
    # Time taken by Thread 2 :  5.00275182723999
    # Time taken by Thread 3 :  5.0025975704193115