#Assignment 2 - Problem 8 - For loop

def numberLength(number):
    
    len1 = len(str(number))

    return len1


def main():
    
    num = input("Enter a number : ")

    if num.isdigit():
        len1 = numberLength(num)
        print("Length of number ", num , " is : ", len1)
    else:
        print("Enter valid number ")
    

if __name__ == "__main__":
    main()


#9. Write a program which accept number from user and return number of digits in that number.
#Input : 5187934 Output : 7

#D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_9.py
#Enter a number : 5187934
#Length of number  5187934  is :  7