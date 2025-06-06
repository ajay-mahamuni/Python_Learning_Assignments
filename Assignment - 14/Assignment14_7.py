#Assignment 14 - Problem 7 - Python OOP imlpementation using class and inheritance

class Person:    

    def __init__(self,pName,pAge):
        self.Name = pName
        self.Age = pAge 

    def Display(self):
        print("Name : ", self.Name,end=" \t")
        print("Age : ", self.Age,end=" \t\n")

class Teacher(Person):
    def __init__(self, tName, tAge,tSubject,tSalary):
        super().__init__(tName, tAge)

        self.Subject = tSubject
        self.Salary = tSalary

    def Display(self):
        print("Name : ", self.Name,end=" \t")
        print("Age : ", self.Age,end=" \t")
        print("Subject : ", self.Subject,end=" \t")
        print("Salary : ", self.Salary,end=" \t\n\n")
        

def main():

    objBase = Person("Person X",25)
    objBase.Display()

    objDerive = Teacher("Person Y",29,"Maths",30000)
    objDerive.Display()    

    objBase2 = Person("Santosh",35)
    objBase2.Display()

    objDerive2 = Teacher("Sakshi",24,"English",42000)
    objDerive2.Display()    

if __name__ == "__main__":
    main()



    # Create a base class Person with name and age. Derive a class Teacher with subject
    # and salary. Use super() to call base class constructor and print both.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_7.py
    # Name :  Person X        Age :  25
    # Name :  Person Y        Age :  29       Subject :  Maths        Salary :  30000

    # Name :  Santosh         Age :  35
    # Name :  Sakshi  Age :  24       Subject :  English      Salary :  42000