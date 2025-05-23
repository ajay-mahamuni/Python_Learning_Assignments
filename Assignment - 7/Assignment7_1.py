#Assignment 7 - Problem 1 - Lambda function to caclculate square and cube of a number

NumberSquare = lambda num : num ** 2

NumberCube = lambda num : num ** 3


def main():
    
    num = input("Enter a number : ")
    

    if num.isdigit():

        numberSquare = NumberSquare(int(num))

        numberCube = NumberCube(int(num))

        print("Square of number ", num , " is : ", numberSquare)

        print("Cube of number ", num , " is : ", numberCube)
        
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()

    # Q1. Write two lambda functions:
    # • One to calculate square of a number
    # • Another to calculate cube of a number
    # Expected Input:
    # Enter a number: 3
    # Expected Output:
    # Square: 9
    # Cube: 27


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_1.py
    # Enter a number : 5
    # Square of number  5  is :  25
    # Cube of number  5  is :  125

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_1.py
    # Enter a number : 10
    # Square of number  10  is :  100
    # Cube of number  10  is :  1000