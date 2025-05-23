#Assignment 6 - Problem 6 - Print Triangle format


def main():

    numberList = input("Enter five numbers separated by space: ")

    numberSplit = numberList.split()

    if len(numberSplit) == 5:
        num1 = numberSplit[0]
        num2 = numberSplit[1]
        num3 = numberSplit[2]
        num4 = numberSplit[3]
        num5 = numberSplit[4]
    
        if num1.isdigit() and num2.isdigit() and num3.isdigit() and num4.isdigit() and num5.isdigit():

            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)
            num4 = int(num4)
            num5 = int(num5)

            if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
                print("Largest number is : ", num1)
            elif num2 > num3 and num2 > num4 and num2 > num5:
                print("Largest number is : ", num2)
            elif num3 > num4 and num3 > num5:
                print("Largest number is : ", num3)
            elif num4 > num5:
                print("Largest number is : ", num4)
            else:
                print("Largest number is : ", num5)

        else:
            print("Enter valid numbers")

    else:
            print("Enter valid numbers")


if __name__ == "__main__":
    main()

    # Q7. Accept 5 numbers from the user. Find and print the largest number.
    # Expected Input:
    # Enter 5 numbers: 23 89 12 56 45
    # Expected Output:
    # Maximum number is: 89


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_7.py
    # Enter five numbers separated by space: 1 2 3 4 5 6
    # Enter valid numbers

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_7.py
    # Enter five numbers separated by space: 1 2 3 4 5
    # Enter valid numbers

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_7.py
    # Enter five numbers separated by space: 1 2 3 4 5
    # Largest number is :  5

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_7.py
    # Enter five numbers separated by space: 1 2 3 5 4
    # Largest number is :  5

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_7.py
    # Enter five numbers separated by space: 1 2 5 3 4
    # Largest number is :  5

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_7.py
    # Enter five numbers separated by space: 1 5 2 3 4
    # Largest number is :  5

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_7.py
    # Enter five numbers separated by space: 5 1 2 3 4
    # Largest number is :  5
