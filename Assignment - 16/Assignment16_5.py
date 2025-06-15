#Assignment 15 - Problem 5 - Python file i/o imlpmentation

import os

def main():        
    
    fObj = open("Demo.txt","r")

    rdata = fObj.readlines()

    for lines in rdata:
        words = lines.split()

        if len(words) > 5:
            print(lines)
    

    fObj.close()

    

if __name__ == "__main__":
    main()


    # 5. Write a program to read a file line by line and display only those lines that contain
    # more than 5 words.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_5.py
    # Amey Mahamuni GGIS School Pimpri Pune

    # Hriyaan Patel Global School Pimpri Pune

    # Rishank Deshmukh Global School Pimpri Pune

    # Rujula Bhagat Global School Pimpri Pune

    # Aarav Deshpande Wisdom School Pimpri Pune