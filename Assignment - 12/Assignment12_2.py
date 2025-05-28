#Assignment 12 - Problem 2 - Python OOP imlpementation using class , class variables, instance  variables and class methods

class Circle:
    PI = 3.14   #class variable declaration

    def __init__(self):
        self.Radius = 0.0              #instance variable declaration
        self.Area = 0.0                    #instance variable declaration
        self.Circumference = 0.0           #instance variable declaration
        
    def Accept(self,cRadius):
        self.Radius = cRadius

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius*self.Radius)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of Circle is : ", self.Radius)
        print("Area of Circle is : ", self.Area)
        print("Circumference of Circle is : ", self.Circumference)

def main():
    rad = input("Enter radius of a circle : ")

    try:
        rad = float(rad)

        objCircle = Circle()

        objCircle.Accept(rad)

        objCircle.CalculateArea()

        objCircle.CalculateCircumference()

        objCircle.Display()

    except Exception as ex:
        print("Enter valid radius..", ex)

if __name__ == "__main__":
    main()


    # 2. Write a program which contains one class named as Circle.
    # Circle class contains three instance variables as Radius ,Area, Circumference.
    # That class contains one class variable as PI which is initialise to 3.14.
    # Inside init method initialise all instance variables to 0.0.
    # There are three instance methods inside class as Accept() ,CalculateArea() ,
    # CalculateCircumference(), Display().
    # Accept method will accept value of Radius from user.
    # CalculateArea() method will calculate area of circle and store it into instance variable Area.
    # CalculateCircumference() method will calculate circumference of circle and store it into instance
    # variable Circumference.
    # And Display() method will display value of all the instance variables as Radius , Area,
    # Circumference.
    # After designing the above class call all instance methods by creating multiple objects.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 12>python Assignment12_2.py
    # Enter radius of a circle : 10
    # Radius of Circle is :  10.0
    # Area of Circle is :  314.0
    # Circumference of Circle is :  62.800000000000004

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 12>python Assignment12_2.py
    # Enter radius of a circle : 15.5
    # Radius of Circle is :  15.5
    # Area of Circle is :  754.385
    # Circumference of Circle is :  97.34