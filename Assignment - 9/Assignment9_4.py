#Assignment 9 - Problem 4 - Multi threaded program to identify letters, capital letter and numbers

import multiprocessing
import multiprocessing.process
import threading
import time

def SumOfNumber(number):
    
    sum = 0

    for i in range(number+1):
        sum = sum + i

    return sum


def main():

    start_time = time.time()

    returnValue = SumOfNumber(1000000)

    end_time = time.time()

    print("Sum using normal function : ", returnValue)
    
    print("Time taken by normal function to execute : ", (end_time - start_time))    

    print(end= " \n")

    T1 = threading.Thread(target=SumOfNumber,args=(1000000,))

    start_time_thred = time.time()

    T1.start()
    
    returnValue = SumOfNumber(10000000)

    T1.join()

    end_time_thread = time.time()

    print("Sum using threading : ", returnValue)
    
    print("Time taken by threading to execute : ", (end_time_thread - start_time_thred))    

    print(end= " \n")

    P1 = multiprocessing.Process(target=SumOfNumber,args=(10000000,))

    start_time_proc = time.time()

    P1.start()
    
    returnValue = SumOfNumber(10000000)

    P1.join()

    end_time_proc = time.time()

    print("Sum using multi processing : ", returnValue)
    
    print("Time taken by multi processing to execute : ", (end_time_proc - start_time_proc))

    print(end= " \n")

if __name__ == "__main__":
    main()


    # 4. Create a Python program that Compare execution time of summing
    # numbers from 1 to 10 million using normal function, threading, and
    # multiprocessing.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 9>python Assignment9_4.py
    # Sum using normal function :  500000500000
    # Time taken by normal function to execute :  0.02875828742980957

    # Sum using threading :  50000005000000
    # Time taken by threading to execute :  0.33826565742492676

    # Sum using multi processing :  50000005000000
    # Time taken by multi processing to execute :  0.3839879035949707
