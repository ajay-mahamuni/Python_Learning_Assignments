#Assignment 6 - Problem 4 - Factorial of a number

def main():
    
    num = input("Enter a number : ")

    result = 1

    if num.isdigit():

        num = int(num) 

        for i in range (1,num + 1):            
            result = result * i

        print("Factorial of number ", num, " is ", result)
            
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()


    # Q4. Accept a number and print its factorial using a for loop.
    # Expected Input:
    # Enter a number: 5
    # Expected Output:
    # Factorial of 5 is: 120


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_4.py
    # Enter a number : 10
    # Factorial of number  10  is  3628800

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_4.py
    # Enter a number : 7
    # Factorial of number  7  is  5040
    