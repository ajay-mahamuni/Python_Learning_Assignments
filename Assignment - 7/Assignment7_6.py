#Assignment 7 - Problem 6 - Check number is prime or not from a list of numbers using filter function

def CheckPrime(num):
    flag = True

    if num == 0 or num == 1: 
        flag = False
    elif num > 1:      
        for no in range(2,num):
            if(num % no) == 0:
                flag = False
                break

    return flag

def main():
    
    size = input("Enter number of elements in list : ")
    

    if size.isdigit():

        dataList = []

        for i in range(int(size)) : 
            no = input()
            if no.isdigit():
                dataList.append(int(no))            

        print("Input data : ",dataList)

        fData = list(filter(CheckPrime,dataList))

        print("Output data : ",fData)
            
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()

    # Q6. Write a function that accepts a list of integers and returns a list of prime numbers
    # using filter().
    # Expected Input:
    # Enter list: 10 11 12 13 14 15 16 17
    # Expected Output:
    # Prime numbers: [11, 13, 17]

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_6.py
    # Enter number of elements in list : 10
    # 10
    # 11
    # 12
    # 13
    # 14
    # 15
    # 16
    # 17
    # 18
    # 19
    # Input data :  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # Output data :  [11, 13, 17, 19]