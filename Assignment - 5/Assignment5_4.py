#Assignment 5 - Problem 4- Find largest number from 3 numbers

def main():

    numberList = input("Enter three numbers separated by space: ")

    numberSplit = numberList.split()

    if len(numberSplit) == 3:
        num1 = numberSplit[0]
        num2 = numberSplit[1]
        num3 = numberSplit[2]
    
        if num1.isdigit() and num2.isdigit() and num3.isdigit():

            num1 = int(num1)
            num2 = int(num2)
            num3 = int(num3)

            if num1 > num2 and num1 > num3:
                print("Largest number is : ", num1)
            elif num2 > num3:
                print("Largest number is : ", num2)
            else:
                print("Largest number is : ", num3)
        else:
            print("Enter valid numbers")

    else:
            print("Enter valid numbers")


if __name__ == "__main__":
    main()


    # Q4. Find Largest Among Three Numbers
    # Accept three numbers from the user and print the largest using nested if-else statements.
    # Expected Input:


    # Enter three numbers: 5 9 3
    # Expected Output:
    # Largest number is 9.


#    D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_4.py
#     Enter three numbers separated by space: 4 7 8
#     Largest number is :  8

#     D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_4.py
#     Enter three numbers separated by space: 8 9 1
#     Largest number is :  9

#     D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_4.py
#     Enter three numbers separated by space: 12 sd 89
#     Enter valid numbers