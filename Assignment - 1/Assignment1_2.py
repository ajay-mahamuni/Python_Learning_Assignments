#Assignment 1 - Problem 2 - Find Even or Odd number
def main():
    print("Enter a number : ")
    num1 = int(input())
    ChkNum(num1)

def ChkNum(number1):

    reminder = number1 % 2

    if reminder == 0:
        print("Entered number ",number1," is Even Number")
    
    if reminder == 1:
        print("Entered number ",number1," is Odd Number")


if __name__ == "__main__":
    main()
