#Assignment 3 - Problem 4 - Frequency of number in a  list

def searchNumber(searchNumber,numList):
    cnt = 0

    for i in numList:
        if searchNumber == i:
            cnt = cnt + 1

    return cnt


def main():
    size = int(input("Enter number of elements : "))

    dataList = []
    num = 0

    if size > 0:
        for i in range(size):

            num = input()

            if num.isdigit():
                dataList.append(int(num))
            else:
                print("Enter valid number")    

        numToSearch = int(input("Element to search : "))

        cnt =  searchNumber(numToSearch,dataList)

        print("Frequency of ",numToSearch," from list is : ", cnt)

if __name__ == "__main__":
    main()


    # 4.Write a program which accept N numbers from user and store it into List. Accept one another
    # number from user and return frequency of that number from List.
    # Input : Number of elements : 11
    # Input Elements : 13 5 45 7 4 56 5 34 2 5 65
    # Element to search : 5
    # Output : 3


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 3>python Assignment3_4.py
    # Enter number of elements : 5
    # 12
    # 45
    # 65
    # 12
    # 28
    # Element to search : 12
    # Frequency of  12  from list is :  2
