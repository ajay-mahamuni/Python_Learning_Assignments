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
    filename = input("Enter a filename :")

    flag = os.path.exists(filename)

    if flag == True:
        fObj = open(filename,"r")        
        data = fObj.read()

        Header()

        print("\n\n\n\n")

        print("--------------------------Content of file-------------------------")

        print("\n\n")

        print(data)

        print("\n\n\n\n")

        Footer()
        fObj.close()
    else:
        print("Provided file does not exist in directory")


if __name__ == "__main__":
    main()


    # 2. Write a program which accept file name from user and open that file and display the contents
    # of that file on screen.
    # Input : Demo.txt
    # Display contents of Demo.txt on console.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 15>python Assignment15_2.py
    # Enter a filename :Demo.txt
    # ---------------------------------------------------------------------
    # ---------------------------Marvellous Automation---------------------
    # ---------------------------------------------------------------------





    # --------------------------Content of file-------------------------



    # "Nature has given us all the pieces required to achieve exceptional wellness and health,
    # but has left it to us to put these pieces together."

    # -Diane McLaren





    # ---------------------------------------------------------------------
    # ------------------Thank you for using our script---------------------
    # ---------------------------AM Consultancy----------------------------
    # ---------------------------------------------------------------------