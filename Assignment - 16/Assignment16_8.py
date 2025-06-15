#Assignment 15 - Problem 6 - Python file i/o imlpmentation

import os
import datetime

def main():        
    
    sfObj = open("Source2.txt","r")

    rdata = sfObj.readlines()

    dateFormat = datetime.datetime.now()

    dateFormat = dateFormat.strftime("%d-%m-%Y").replace("-","") +"-"+ dateFormat.strftime("%X").replace(":","")

    destFileName = "Destination"+dateFormat+".txt"

    dfObj = open(destFileName,"w")

    for lines in rdata:
        if len(lines) > 1:
            dfObj.write(lines)
    

    print("New file created with name : ",destFileName)

    sfObj.close()

    dfObj.close()

    

if __name__ == "__main__":
    main()


    # 8. Write a script to remove all blank lines from a file. Save the cleaned output to a
    # new file.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_8.py
    # New file created with name :  Destination13062025-184932.txt