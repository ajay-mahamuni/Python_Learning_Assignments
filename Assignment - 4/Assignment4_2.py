#Assignment 4 - Problem 2 - Lambda function to calculate power of 2

Multiply = lambda num1,num2 : num1 * num2

def main():
    num1 = input("Enter first number : ")
    num2 = input("Enter first number : ")

    if num1.isdigit() and num2.isdigit():
        
        #call of lambda funtion and convert input number to integer
        multNumber = Multiply(int(num1),int(num2))

        print("Multiplication of two numbers is ", multNumber)

    else:
        print("Enter valid number..")

if __name__ == "__main__":
    main()


    # 2.Write a program which contains one lambda function which accepts two parameters and return
    # its multiplication.
    # Input : 4 3 Output : 12
    # Input : 6 3 Output : 18

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 4>python Assignment4_2.py
    # Enter first number : 15
    # Enter first number : 20
    # Multiplication of two numbers is  300
