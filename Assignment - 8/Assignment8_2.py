#Assignment 8 - Problem 2 - Multi threaded program for sum of even and odd numbers

import threading
import os

CheckEven = lambda num : True if num % 2 == 0 else False

def EvenFactor(cntr):
    
    result = 0
    datalist= []

    for i in range(1,cntr):
        if cntr % i == 0 and CheckEven(i): #check the value is factor of given number and is an even number then add to list
            datalist.append(i)

            result = result + i
    
    print("Even Factors : ", datalist)
    
    print("Sum of Even Factors : ", result)

    

def OddFactor(cntr):
    
    result = 0
    datalist= []

    for i in range(1,cntr):
        if cntr % i == 0 and CheckEven(i) == False: #check the value is factor of given number and is an odd number then add to list
            datalist.append(i)

            result = result + i
    
    print("Odd Factors : ", datalist)
    
    print("Sum of Odd Factors : ", result)

        

def main():   

    num = input("Enter a number : ")

    if num.isdigit():        

        num = int(num)

        T1 = threading.Thread(target=EvenFactor,args=(num,))

        T2 = threading.Thread(target=OddFactor,args=(num,))

        T1.start()

        T2.start()

        T1.join()

        T2.join()

    else:
        print("Enter valid number..")


    print("Exit from main...")
    
if __name__ == "__main__":
    main()

    # 2.Design python application which creates two threads as evenfactor and oddfactor.
    # Both the thread accept one parameter as integer. Evenfactor thread will display
    # addition of even factors of given number and oddfactor will display addition of odd
    # factors of given number. After execution of both the thread gets completed main
    # thread should display message as “exit from main”.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 8>python Assignment8_2.py
    # Enter a number : 100
    # Even Factors :  [2, 4, 10, 20, 50]
    # Sum of Even Factors :  86
    # Odd Factors :  [1, 5, 25]
    # Sum of Odd Factors :  31
    # Exit from main...