#Assignment 4 - Problem 1 - Lambda function to calculate power of 2

Power = lambda num1 : num1 ** 2

def main():
    num1 = input("Enter a number : ")

    if num1.isdigit():
        
        #call of lambda funtion and convert input number to integer
        powerofNumber = Power(int(num1))

        print("Power of 2 of number ", num1, " is : ", powerofNumber)

    else:
        print("Enter valid number..")

if __name__ == "__main__":
    main()


    # 1.Write a program which contains one lambda function which accepts one parameter and return
    # power of two.
    # Input : 4 Output : 16
    # Input : 6 Output : 64

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 4>python Assignment4_1.py
    # Enter a number : 15
    # Power of 2 of number  15  is :  225