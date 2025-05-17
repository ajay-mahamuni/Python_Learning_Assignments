#Assignment 2 - Problem 8 - For loop

def numberSum(number):
    sum = 0
    for i in number:
        sum = sum + int(i)

    return sum


def main():
    
    num = input("Enter a number : ")

    if num.isdigit():
        sum = numberSum(str(num))
        print("Sum of number ", num , " is : ", sum)
    else:
        print("Enter valid number ")    

if __name__ == "__main__":
    main()



    #10. Write a program which accept number from user and return addition of digits in that number.
    #Input : 5187934 Output : 37
    
    #D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_10.py
    #Enter a number : 5187934
    #Sum of number  5187934  is :  37
