#Assignment 8 - Problem 4 - Multi threaded program to identify letters, capital letter and numbers

import threading



def ThreadLowerCase(str):    

    try:
        print("Thread id of LowerCase : ", threading.get_ident())            
        resultStr = ""

        for char in str:
               if char.isupper():
                   resultStr = resultStr + char

        print("Uppercase characters : ",resultStr)

    except Exception as ex:
        print("Error : ", ex)

def ThreadUpperCase(str):

    try:
        print("Thread id of UpperCase : ", threading.get_ident())      
        resultStr = ""

        for char in str:
               if char.islower():
                   resultStr = resultStr + char
        print("Lowercase characters : ",resultStr)

    except Exception as ex:
        print("Error : ", ex)

def ThreadDigit(str):

    try:
        print("Thread id of Digit : ", threading.get_ident())      

        resultStr = ""

        for char in str:
               if char.isdigit():
                   resultStr = resultStr + char

        print("Digits : ",resultStr)

    except Exception as ex:
        print("Error : ", ex)


        

def main():   

    inputString = input("Enter a string : ")
     
    
     

    if len(inputString) > 0:

        try:
        
            T1 = threading.Thread(target=ThreadLowerCase,args=(inputString,))

            T2 = threading.Thread(target=ThreadUpperCase,args=(inputString,))

            T3 = threading.Thread(target=ThreadDigit,args=(inputString,))

            T1.start()

            T2.start()

            T3.start()

            T1.join()

            T2.join()

            T3.join()

        except Exception as exObj:
            print("Exception occured : ",exObj)

    else:
        print("Enter valid string..")


    
if __name__ == "__main__":
    main()

    # 4.Design python application which creates three threads as small, capital, digits. All the
    # threads accepts string as parameter. Small thread display number of small characters,
    # capital thread display number of capital characters and digits thread display number of
    # digits. Display id and name of each thread.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 8>python Assignment8_4.py
    # Enter a string : hkjhkjh687687TUYYTVGF&*()%$LKJLKJjgjhg124343
    # Thread id of LowerCase :  23180
    # Thread id of UpperCase :  32600
    # Uppercase characters :  TUYYTVGFLKJLKJ
    # Thread id of Digit :  29472
    # Lowercase characters :  hkjhkjhjgjhg
    # Digits :  687687124343