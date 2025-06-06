#Assignment 14 - Problem 1 - Python OOP imlpementation using class and instance methods

class Employee:    

    def __init__(self,eName,eEmployeeId,eSalary):
        self.Name = eName
        self.EmployeeId = eEmployeeId
        self.Salary = eSalary

    def Display(self):
        print("Name : ", self.Name,end = " \t")
        print("Employee Id : ", self.EmployeeId,end = " \t")
        print("Salary : ", self.Salary,end = " \t\n")

def main():
    obj1 = Employee("Ajay",1,50000)
    obj2 = Employee("Mayuri",2,45000)
    obj3 = Employee("Amey",3,30000)

    obj1.Display()
    obj2.Display()
    obj3.Display()
    

if __name__ == "__main__":
    main()


    # 1. Create a class Employee with attributes name, emp_id, and salary. Create objects
    # of this class and print their details using a method.
    # Expected Output:
    # Name: Rohit, ID: 101, Salary: 50000


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_1.py
    # Name :  Ajay    Employee Id :  1        Salary :  50000
    # Name :  Mayuri  Employee Id :  2        Salary :  45000
    # Name :  Amey    Employee Id :  3        Salary :  30000