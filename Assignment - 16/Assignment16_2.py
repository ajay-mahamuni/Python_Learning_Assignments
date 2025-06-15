#Assignment 15 - Problem 2 - Python file i/o imlpmentation

import os

def Header():
    print("---------------------------------------------------------------------")
    print("---------------------------Marvellous Automation---------------------")
    print("---------------------------------------------------------------------")

def Footer():
    print("---------------------------------------------------------------------")
    print("------------------Thank you for using our script---------------------")
    print("---------------------------AM Consultancy----------------------------")
    print("---------------------------------------------------------------------")


def main():    
    
    fObj = open("Student.txt","r")

    rdata = fObj.read()

    Header()

    print("---------------------------Content of file---------------------------")
    print("\n\n")

    print(rdata)

    Footer()

    fObj.close()

if __name__ == "__main__":
    main()


    # 2. Write a program to read and display the contents of a file data.txt.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_2.py
    # ---------------------------------------------------------------------
    # ---------------------------Marvellous Automation---------------------
    # ---------------------------------------------------------------------
    # ---------------------------Content of file---------------------------



    # Amey Mahamuni
    # Hriyaan Patel
    # Rishank Deshmukh
    # Rujula Bhagat
    # Aarav Deshpande

    # ---------------------------------------------------------------------
    # ------------------Thank you for using our script---------------------
    # ---------------------------AM Consultancy----------------------------
    # ---------------------------------------------------------------------