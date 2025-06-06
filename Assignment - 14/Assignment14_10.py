#Assignment 14 - Problem 10 - Python OOP imlpementation using class and instance methods

class Employee:
    def __init__(self,eName,eDepartment,eSalary):
        self.Name = eName               #public variable
        self._Department = eDepartment  #protected variable
        self.__Salary = eSalary         #private variable

    def Display(self):
        print("Inside Class display..")

        print("Name : ",self.Name,end=" \t") 
        print("Department : ",self._Department,end=" \t")
        print("Salary : ",self.__Salary,end=" \t\n\n")
        

def main():
    obj = Employee("Ajay","Marketing",25000)
    obj.Display()

    print("Inside Main method..")
    obj = Employee("Mayuri","HR",18000)
    print("Name : ",obj.Name,end=" \t") 
    print("Department : ",obj._Department,end=" \t")


if __name__ == "__main__":
    main()


    # 10. Demonstrate private, protected and public access modifiers using a class Employee
    # with attributes: __salary, _department, name.
    

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_10.py
    # Inside Class display..
    # Name :  Ajay    Department :  Marketing         Salary :  25000

    # Inside Main method..
    # Name :  Mayuri  Department :  HR