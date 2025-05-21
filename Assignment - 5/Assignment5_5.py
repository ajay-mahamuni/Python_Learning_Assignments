#Assignment 5 - Problem 5- Check even or odd number

# def CheckEvenOdd(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

CheckEvenOdd = lambda num: True if num % 2 == 0 else False
        

def main():

    number = input("Enter a numbers : ")

    if number.isdigit() :
        if CheckEvenOdd(int(number)):
            print(number, " is a Even number.")
        else:
            print(number, " is an Odd number.")            
    else:
        print("Enter valid number")

    

if __name__ == "__main__":
    main()



    # Q5. Even or Odd Number Check
    # Write a program to check whether the entered number is even or odd.
    # Expected Input:
    # Enter a number: 17
    # Expected Output:
    # 17 is an odd number.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_5.py
    # Enter a numbers : 21
    # 21  is an Odd number.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_5.py
    # Enter a numbers : 0
    # 0  is a Even number.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_5.py
    # Enter a numbers : 100
    # 100  is a Even number.