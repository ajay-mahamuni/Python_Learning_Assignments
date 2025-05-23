#Assignment 8 - Problem 1 - Create threads for even and odd numbers

import threading
import os

def ShowEven(cntr):
    
    cnt = 0
    i = 0
    datalist= []
    while(i < cntr):
        if cnt % 2 == 0:
            datalist.append(cnt)
            i = i +1
            
        cnt = cnt + 1

    print("Even Number : ", datalist)

    

def ShowOdd(cntr):
    
    cnt = 1
    i = 0
    datalist= []
    while(i < cntr):
        if cnt % 2 != 0:
            datalist.append(cnt)
            i = i +1
            
        cnt = cnt + 1

    print("Odd Number : ", datalist)

        

def main():   

    Even = threading.Thread(target=ShowEven,args=(10,))

    Odd = threading.Thread(target=ShowOdd,args=(10,))

    Even.start()

    Odd.start()

    Even.join()

    Odd.join()
    
if __name__ == "__main__":
    main()

    # 1.Design python application which creates two thread named as even and odd. Even
    # thread will display first 10 even numbers and odd thread will display first 10 odd
    # numbers.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 8>python Assignment8_1.py
    # Even Number :  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    # Odd Number :  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]