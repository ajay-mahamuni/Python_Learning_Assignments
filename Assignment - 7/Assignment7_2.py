#Assignment 7 - Problem 2 - Use of map function to double the number

NumberDouble = lambda num : num + num

def main():
    
    size = input("Enter number of elements in list : ")
    

    if size.isdigit():

        dataList = []

        for i in range(int(size)) : 
            no = input()
            if no.isdigit():
                dataList.append(int(no))            

        print("Input data : ",dataList)

        mData = list(map(NumberDouble,dataList))

        print("Output data : ",mData)

        
    else:
        print("Enter valid number")
    
if __name__ == "__main__":
    main()

    # Q2. Accept a list of integers from the user and use the map() function to double each value.
    # Expected Input:
    # Enter list: 1 2 3 4 5
    # Expected Output:
    # Doubled list: [2, 4, 6, 8, 10]


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_2.py
    # Enter number of elements in list : 5
    # 2
    # 4
    # 8
    # 9
    # 12
    # Input data :  [2, 4, 8, 9, 12]
    # Output data :  [4, 8, 16, 18, 24]

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 7>python Assignment7_2.py
    # Enter number of elements in list : 4
    # 3
    # 6
    # 9
    # 12
    # Input data :  [3, 6, 9, 12]
    # Output data :  [6, 12, 18, 24]