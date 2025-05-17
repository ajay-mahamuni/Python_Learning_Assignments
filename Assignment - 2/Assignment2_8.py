#Assignment 2 - Problem 8 - For loop

def forloop(number):
    
    for i in range(number+1):

        for j in range(1,i+1):

            print(j,end = " ")            

        print(end = " \n")
        


def main():
    
    num = int(input("Enter a number : "))

    forloop(num)

if __name__ == "__main__":
    main()


    #8. Write a program which accept one number and display below pattern.
    #Input : 5
    #Output : 
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5

    #D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_8.py
    #Enter a number : 5

    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5
