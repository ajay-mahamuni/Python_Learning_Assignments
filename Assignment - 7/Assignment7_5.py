#Assignment 7 - Problem 2 - Use of reduce function to muliply numbers from list

def main():
    
    str = input("Enter a string : ")

    revStrList = list(reversed(str))

    revStr = ""

    for i in revStrList:
        revStr= revStr + i


    print("Input string : ", str)
    
    print("Reversed string : ", revStr)

    if str == revStr:
        print(str, " is a palindrome")
    else:
        print(str, " is not a palindrome")
    

    
if __name__ == "__main__":
    main()

    # Q5. Write a function that accepts a string and checks whether it is a palindrome.
    # Expected Input:
    # Enter a string: radar
    # Expected Output:radar is a palindrome.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_5.py
    # Enter a string : naman
    # Input string :  naman
    # Reversed string :  naman
    # naman  is a palindrome

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_5.py
    # Enter a string : Marvellous
    # Input string :  Marvellous
    # Reversed string :  suollevraM
    # Marvellous  is not a palindrome