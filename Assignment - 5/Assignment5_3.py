#Assignment 5 - Problem 3 - Check the age of a person

def CheckAge(age):        
    if age>= 18:
        print("Person is eligible for vote")
    else:
        print("Person is not eligible for vote")
    
def main():

    age = input("Enter age of a person : ")

    if age.isdigit():
        CheckAge(int(age))
    else:
        print("Enter valid age")

if __name__ == "__main__":
    main()


    # Q3. Voting Eligibility Checker
    # Accept age from the user and check whether the person is eligible to vote. (Age should be
    # 18 or above.)
    # Expected Input:
    # Enter age: 19
    # Expected Output:
    # Eligible to vote.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_3.py
    # Enter age of a person : 15
    # Person is not eligible for vote

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_3.py
    # Enter age of a person : 18
    # Person is eligible for vote

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_3.py
    # Enter age of a person : 99
    # Person is eligible for vote

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_3.py
    # Enter age of a person : ad
    # Enter valid age