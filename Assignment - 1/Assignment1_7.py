#Assignment 1 - Problem 7 - Number Division
def main():
    print("Enter a number : ")
    num1 = int(input())
    ChkNum(num1)

def ChkNum(number1):

    reminder = number1 % 5

    if reminder == 0:
        print("True - Entered number ",number1," is divisible by 5")
    
    if reminder != 0:
        print("False - Entered number ",number1," is NOT divisible by 5")


if __name__ == "__main__":
    main()