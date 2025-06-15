#Assignment 15 - Problem 7 - Python file i/o imlpmentation

def main():        
    
    fObj = open("Marks.txt","r")

    rdata = fObj.readlines()

    for lines in rdata:

        words = lines.split()
        
        for word in words:
            if word.isdigit():
                if int(word) > 75:
                    print(lines)


        

    fObj.close()

    

if __name__ == "__main__":
    main()


    # 7. Create a file marks.txt with student name and marks. Then read the file and
    # display students who scored more than 75 marks.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 16>python Assignment16_7.py
    # Amey Mahamuni   89

    # Rishank Deshmukh        95

    # Rujula Bhagat   85