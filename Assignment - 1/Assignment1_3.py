#Assignment 1 - Problem 3 - Addition of two numbers
def main():
    print("Enter first number : ")
    number1 = float(input())

    print("Enter second number : ")
    number2 = float(input())

    output = Addition(number1, number2)

    print("Addition of two numbers is : ", output)

def Addition(num1, num2):
    result = 0

    result = float(num1) + float(num2)

    return result

if __name__ == "__main__":
    main()