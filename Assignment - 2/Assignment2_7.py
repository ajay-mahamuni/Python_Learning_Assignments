#Assignment 2 - Problem 7 - For loop

def forloop(number):
    
    for no in range(number):        

        for i in range(1,number+1):
            
            print(i,end = " ")
        
        print(end = " \n")


def main():

    num = int(input("Enter a number : "))

    forloop(num)

if __name__ == "__main__":
    main()


    #7. Write a program which accept one number and display below pattern.
    #Input : 5
    #Output : 
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5


    #D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 2>python Assignment2_7.py
    #Enter a number : 5

    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5