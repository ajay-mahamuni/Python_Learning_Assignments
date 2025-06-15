#Assignment 15 - Problem 6 - Python file i/o imlpmentation

import os
import datetime

def main():        
    
    sfObj = open("Source.txt","r")

    rdata = sfObj.read()

    dateFormat = datetime.datetime.now()

    dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%X").replace(":","")

    destFileName = "Destination"+dateFormat+".txt"

    dfObj = open(destFileName,"w")

    dfObj.write(rdata)

    print("New file created with name : ",destFileName)

    sfObj.close()

    dfObj.close()

    

if __name__ == "__main__":
    main()


    # 6. Write a Python program to copy the contents of one file (source.txt) into another
    # file (destination.txt).

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_6.py
    # New file created with name :  Destination13062025-180615.txt