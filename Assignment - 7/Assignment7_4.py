#Assignment 7 - Problem 4 - Use of reduce function to muliply numbers from list

from functools import reduce

NumberMultiply = lambda num1,num2 : num1 * num2

def main():
    
    size = input("Enter number of elements in list : ")
    

    if size.isdigit():

        dataList = []

        for i in range(int(size)) : 
            no = input()
            if no.isdigit():
                dataList.append(int(no))            

        print("Input data : ",dataList)

        rData = reduce(NumberMultiply,dataList)

        print("Output data : ",rData)

        
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()

    # Q4. Accept a list of numbers and use reduce() (from functools) to find the product of
    # all numbers.
    # Expected Input:
    # Enter list: 2 3 4
    # Expected Output:
    # Product: 24


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_4.py
    # Enter number of elements in list : 4
    # 1
    # 2
    # 3
    # 4
    # Input data :  [1, 2, 3, 4]
    # Output data :  24

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_4.py
    # Enter number of elements in list : 5
    # 10
    # 20
    # 30
    # 40
    # 50
    # Input data :  [10, 20, 30, 40, 50]
    # Output data :  12000000

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_4.py
    # Enter number of elements in list : 4
    # 11
    # 21
    # 51
    # 101
    # Input data :  [11, 21, 51, 101]
    # Output data :  1189881