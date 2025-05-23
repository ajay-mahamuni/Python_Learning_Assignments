#Assignment 7 - Problem 3 - Use of filter function to keep even numbers from list

CheckEven = lambda num : True if num % 2 == 0 else False

def main():
    
    size = input("Enter number of elements in list : ")
    

    if size.isdigit():

        dataList = []

        for i in range(int(size)) : 
            no = input()
            if no.isdigit():
                dataList.append(int(no))            

        print("Input data : ",dataList)

        fData = list(filter(CheckEven,dataList))

        print("Output data : ",fData)

        
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()

    # Q3. Accept a list of numbers and use filter() to keep only even numbers.
    # Expected Input:
    # Enter list: 1 2 3 4 5 6
    # Expected Output:
    # Even numbers: [2, 4, 6]


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_3.py
    # Enter number of elements in list : 6
    # 45
    # 12
    # 45
    # 9
    # 6
    # 2
    # Input data :  [45, 12, 45, 9, 6, 2]
    # Output data :  [12, 6, 2]

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_3.py
    # Enter number of elements in list : 5
    # 0
    # 99
    # 998
    # 9999
    # 10000
    # Input data :  [0, 99, 998, 9999, 10000]
    # Output data :  [0, 998, 10000]