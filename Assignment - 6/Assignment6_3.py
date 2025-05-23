#Assignment 6 - Problem 3 - Mulitplication of numbers

def main():

    result = 0

    num = input("Enter a number : ")

    if num.isdigit():
        for i in range(1,11):            
            print(num, " * ", i, " = ", int(num)*i)
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()


    # Q3. Accept a number from the user and print its multiplication table up to 10.
    # Expected Input:
    # Enter a number: 7
    # Expected Output
    # 7 x 1 = 7
    # 7 x 2 = 14
    # ...
    # 7 x 10 = 70


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 6>python Assignment6_3.py
    # Enter a number : 15
    # 15  *  1  =  15
    # 15  *  2  =  30
    # 15  *  3  =  45
    # 15  *  4  =  60
    # 15  *  5  =  75
    # 15  *  6  =  90
    # 15  *  7  =  105
    # 15  *  8  =  120
    # 15  *  9  =  135
    # 15  *  10  =  150

    