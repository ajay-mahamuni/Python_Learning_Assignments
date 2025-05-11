#Assignment 1 - Problem 6 - Find number status
def main():
    print("Enter a number : ")
    num1 = int(input())
    NumberStatus(num1)

def NumberStatus(number1):

    if number1 == 0:
        print("Entered number ", number1," is Zero")
    
    if number1 > 0:
        print("Entered number ", number1," is Positive number")
    elif number1 < 0:
        print("Entered number ", number1," is Negative number")


if __name__ == "__main__":
    main()
