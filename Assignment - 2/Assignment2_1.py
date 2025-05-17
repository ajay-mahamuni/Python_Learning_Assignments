#Assignment 2 - Problem 1 - Arithmatic operation

from Arithmatic_Module import Add, Sub, Mult, Div # type: ignore

def main():

    num1 = int(input("Enter first number : "))

    num2 = int(input("Enter second number : "))

    op = str(input("Enter arithmatic operation... 1.Add 2.Sub 3.Mult 4.Div : "))

    result = 0

    if op == "Add":
        result = Add(num1,num2)
        print("Addition of two numbers is : ", result)
    elif op == "Sub":
        result = Sub(num1,num2)
        print("Subtraction of two numbers is : ", result)
    elif op == "Mult":
        result = Mult(num1,num2)
        print("Multiplication of two numbers is : ", result)        
    elif op == "Div":
            if (num1 < num2):
                 print("First number should be greater that second number")
            else:
                result = Div(num1,num2)
                print("Divison of two numbers is : ", result)
    else:
        print("Invalid arithmatich operation")



if __name__ == "__main__":
    main()


    #1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
    # for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
    # parameters as number and perform the operation. Write on python program which call all the
    # functions from Arithmetic module by accepting the parameters from user.

    #D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_1.py
    # Enter first number : 15
    # Enter second number : 25
    # Enter arithmatic operation... 1.Add 2.Sub 3.Mult 4.Div : Mult
    # Multiplication of two numbers is :  375
