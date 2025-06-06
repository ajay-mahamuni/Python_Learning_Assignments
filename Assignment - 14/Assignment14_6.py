#Assignment 14 - Problem 6 - Python OOP imlpementation using class and instance methods

class Calculator:    

    def __init__(self):

        self.num1 = input("Enter First number : ")
        self.num2 = input("Enter Second number : ")

        if self.num1.isdigit() and self.num2.isdigit():
            self.num1 = int(self.num1)
            self.num2 = int(self.num2)
        else:
            print("Enter valid numbers.")
        
    def Display(self):
        
        ans = self.Add()
        print("Addition of numbers ", self.num1, " & ",self.num2," is : ",ans)

        ans = self.Sub()
        print("Substraction of numbers ", self.num1, " & ",self.num2," is : ",ans)

        ans = self.Mult()
        print("Multiplication of numbers ", self.num1, " & ",self.num2," is : ",ans)

        ans = self.Mult()
        print("Division of numbers ", self.num1, " & ",self.num2," is : ",ans)

    def Add(self):
        ans = self.num1 + self.num2
        return ans
    
    def Sub(self):
        ans = self.num1 - self.num2
        return ans
    

    def Mult(self):
        ans = self.num1 * self.num2
        return ans
    
    def Div(self):
        ans = self.num1 / self.num2
        return ans


def main():

    obj1 = Calculator()    
    obj1.Display()
    

if __name__ == "__main__":
    main()


    # Create a class Calculator with methods for add, subtract, multiply, divide. Ask user
    # input for values and call methods accordingly.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_6.py
    # Enter First number : 15
    # Enter Second number : 5
    # Addition of numbers  15  &  5  is :  20
    # Substraction of numbers  15  &  5  is :  10
    # Multiplication of numbers  15  &  5  is :  75
    # Division of numbers  15  &  5  is :  75

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_6.py
    # Enter First number : 250
    # Enter Second number : 75
    # Addition of numbers  250  &  75  is :  325
    # Substraction of numbers  250  &  75  is :  175
    # Multiplication of numbers  250  &  75  is :  18750
    # Division of numbers  250  &  75  is :  18750

