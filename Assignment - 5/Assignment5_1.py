#Assignment 5 - Problem 1 - Arithmatic operations of two numbers

def Add(number1, number2):
    return int(number1 + number2)


def Sub(number1, number2):
    return int(number1 - number2)

def Mult(number1, number2):
    return int(number1 * number2)

def Div(number1, number2):
    return int(number1 / number2)

def main():

    num1 = input("Enter first number : ")

    num2 = input("Enter second number : ")

    print("---------Output--------")
    
    result = 0

    if num1.isdigit() and num2.isdigit():
    
            result = Add(int(num1),int(num2))
            print("Addition : ", result)
            
            result = Sub(int(num1),int(num2))
            print("Subtraction : ", result)

            result = Mult(int(num1),int(num2))
            print("Multiplication : ", result)        
            
            result = Div(int(num1),int(num2))
            print("Divison : ", result)
    else:
         print("Invalid input")

if __name__ == "__main__":
    main()


    # Q1. Arithmetic Operations on Two Numbers
    # Write a program to accept two integers from the user and display their:
    # • Sum
    # • Difference
    # • Product
    # • Division
    # Expected Input:
    # Enter first number: 10
    # Enter second number: 2
    # Expected Output:
    # Sum: 12
    # Difference: 8
    # Product: 20
    # Division: 5.0


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_1.py
    # Enter first number : 16
    # Enter second number : 8
    # ---------Output--------
    # Addition :  24
    # Subtraction :  8
    # Multiplication :  128
    # Divison :  2