#Assignment 14 - Problem 4 - Python OOP imlpementation using class and instance methods

class Student:    

    School_Name = "GGIS"

    def __init__(self,sName,sRollNo):
        self.Name = sName
        self.RollNo = sRollNo  

    def Display(self):
        print("School Name : ", Student.School_Name, end=" \t")
        print("Student Name : ", self.Name, end=" \t")
        print("Roll Number : ", self.RollNo, end=" \t\n")

def main():

    obj1 = Student("Amey",5)
    obj2 = Student("Arnav",6)    

    obj1.Display()
    obj2.Display()

    obj3 = Student("Akash",1)    
    Student.School_Name = "HA School"

    obj3.Display()
    

if __name__ == "__main__":
    main()



    # 4. Create a class Student with name, roll_no, and a class variable school_name. Print
    # student details and school name. Change the school name using class name.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_4.py
    # School Name :  GGIS       Student Name :  Amey    Roll Number :  5
    # School Name :  GGIS       Student Name :  Arnav   Roll Number :  6
    # School Name :  HA School  Student Name :  Akash   Roll Number :  1