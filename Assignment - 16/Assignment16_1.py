#Assignment 15 - Problem 1 - Python file i/o imlpmentation

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
    
    data = []
    print("Enter 5 students names : ")
    fObj = open("Student.txt","w")

    

    for i in range(5):
        fObj.write(input()+"\n")    

    fObj.close()

    fObj = open("Student.txt","r")

    rdata = fObj.read()

    Header()

    print("------------Content of file-----------")
    print("\n\n\n\n")

    print(rdata)

    Footer()




if __name__ == "__main__":
    main()


    # 1. Write a Python program to create a text file named student.txt and write the
    # names of 5 students into it.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_1.py
    # Enter 5 students names :
    # Amey Mahamuni
    # Rishank Deshmukh
    # Hriyaan Patel
    # Rujula Bhagat
    # Aarav Deshpande
    # ---------------------------------------------------------------------
    # ---------------------------Marvellous Automation---------------------
    # ---------------------------------------------------------------------
    # ------------Content of file-----------





    # Amey Mahamuni
    # Rishank Deshmukh
    # Hriyaan Patel
    # Rujula Bhagat
    # Aarav Deshpande

    # ---------------------------------------------------------------------
    # ------------------Thank you for using our script---------------------
    # ---------------------------AM Consultancy----------------------------
    # ---------------------------------------------------------------------