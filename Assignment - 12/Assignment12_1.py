#Assignment 12 - Problem 1 - Python OOP imlpementation using class and instance methods

class Demo:

    Value = 0

    def __init__(self,num1,num2):
        self.Num1 = num1
        self.Num2 = num2

    def fun(self):
        print("Inside fun...")
        print("Value of num1 : ", self.Num1)
        print("Value of num2 : ", self.Num2)

    def gun(self):
        print("Inside gun...")
        print("Value of num1 : ", self.Num1)
        print("Value of num2 : ", self.Num2)

def main():
    no1 = input("Enter first number : ")

    no2 = input("Enter second number : ")

    if no1.isdigit() and no2.isdigit():
        obj1 = Demo(int(no1),int(no2))

        obj2 = Demo(int(no1),int(no2))

        obj1.fun()

        obj1.gun()

        obj2.fun()

        obj2.gun()
    else:
        print("Enter valid numbers.")

if __name__ == "__main__":
    main()