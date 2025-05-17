#Assignment 2 - Problem 5 - Program to find number is prime or not


def isPrime(number):

    flag = True

    if number == 0 or number == 1: 
        flag = False
    elif number > 1:      
        for no in range(2,number):
            if(number % no) == 0:
                flag = False
                break

    return flag
    
    

def main():    
    
    num = int(input("Enter a number : "))
    
    flag = isPrime(num)
    
    if flag:
        print("Entered number ", num, " is a Prime Number")
    else:
        print("Entered number ", num, " is not a Prime Number")

if __name__ == "__main__":
    main()


    #5.Write a program which accept one number for user and check whether number is prime or not.
    #Input : 5 Output : It is Prime Number

    #D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_5.py
    # Enter a number : 5
    # Entered number  5  is a Prime Number
