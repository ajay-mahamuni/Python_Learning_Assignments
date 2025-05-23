#Assignment 6 - Problem 5 - Check number is prime or not

def CheckPrime(num):
    flag = True

    if num == 0 or num == 1: 
        flag = False
    elif num > 1:      
        for no in range(2,num):
            if(num % no) == 0:
                flag = False
                break

    return flag

def main():
    
    num = input("Enter a number : ")
    

    if num.isdigit():

        num = int(num) 

        if  CheckPrime(num) :
            print("Entered number ", num , " is a Prime number.")
        else:
            print("Entered number ", num , " is not a Prime number.")
            
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()


    # Q5. Accept a number from the user and check whether it is prime or not.
    # Expected Input:
    # Enter a number: 11
    # Expected Output:
    # 11 is a prime number.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_5.py
    # Enter a number : 11
    # Entered number  11  is a Prime number.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_5.py
    # Enter a number : 10
    # Entered number  10  is not a Prime number.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_5.py
    # Enter a number : 121
    # Entered number  121  is not a Prime number.

