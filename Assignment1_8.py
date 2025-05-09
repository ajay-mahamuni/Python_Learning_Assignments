#Assignment 1 - Problem 8 - For loop usage
def main():

    print("Enter a number : ")

    number1 = int(input())

    forLoop(number1)

def forLoop(num):
    for no in range(0,num):
        print("*")

if __name__ == "__main__":
    main()
