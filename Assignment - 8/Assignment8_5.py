#Assignment 8 - Problem 5 - Multi threaded program forward and reverse loop and scheduling of threads

import threading

def Thread1():
    print("Thread 1 id : ", threading.get_ident())            
        
    for i in range(1,51):
         print(i, end = " ")
    
    print(end = " \n")
    

def Thread2():
    print("Thread 2 id : ", threading.get_ident())            
    
    for i in range(50,0,-1):
         print(i, end = " ")
    
    print(end = " \n")
    
        

def main():   

    
        T1 = threading.Thread(target=Thread1)

        T2 = threading.Thread(target=Thread2)

        T1.start()

        T1.join()

        T2.start()        

        T2.join()

    
if __name__ == "__main__":
    main()

    # 5.Design python application which contains two threads named as thread1 and thread2.
    # Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
    # screen. After execution of thread1 gets completed then schedule thread2.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 8>python Assignment8_5.py
    # Thread 1 id :  23108
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
    # Thread 2 id :  36792
    # 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1