#Assignment 12 - Problem 2 - Python OOP imlpementation using class , class variables, instance  variables and class methods

class Arithmetic:
    

    def __init__(self):
        self.Value1 = 0              #instance variable declaration
        self.Value2 = 0              #instance variable declaration
        self.Result = 0             #instance variable declaration
        
        
    def Accept(self,aValue1, aValue2):
        self.Value1 = aValue1
        self.Value2 = aValue2

    def Addition(self):
        result = self.Value1 + self.Value2
        return result

    def Subtraction(self):
        result = self.Value1 - self.Value2
        return result

    def Multiplication(self):
        result = self.Value1 * self.Value2
        return result

    def Division(self):
        result = self.Value1 / self.Value2
        return result

    
def main():
    firstNum = input("Enter first number : ")
    secNum = input("Enter second number : ")

    try:
        

        objArithmatic = Arithmetic()

        objArithmatic.Accept(int(firstNum),int(secNum))

        returnResult = 0

        returnResult = objArithmatic.Addition()

        print("Addition of number ",firstNum ," and ",  secNum, " is : ", returnResult)

        returnResult = objArithmatic.Subtraction()

        print("Subtraction of number ",firstNum ," and ",  secNum, " is : ", returnResult)

        returnResult = objArithmatic.Multiplication()

        print("Multiplication of number ",firstNum ," and ",  secNum, " is : ", returnResult)

        returnResult = objArithmatic.Division()

        print("Division of number ",firstNum ," and ",  secNum, " is : ", returnResult)

    except Exception as ex:
        print("Enter valid radius..", ex)

if __name__ == "__main__":
    main()


    # 3. Write a program which contains one class named as Arithmetic.
    # Arithmetic class contains three instance variables as Value1 ,Value2.
    # Inside init method initialise all instance variables to 0.
    # There are three instance methods inside class as Accept(), Addition(), Subtraction(),
    # Multiplication(), Division().
    # Accept method will accept value of Value1 and Value2 from user.
    # Addition() method will perform addition of Value1 ,Value2 and return result.
    # Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
    # Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
    # Division() method will perform division of Value1 ,Value2 and return result.
    # After designing the above class call all instance methods by creating multiple objects.



    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 12>python Assignment12_3.py
    # Enter first number : 4
    # Enter second number : 2
    # Addition of number  4  and  2  is :  6
    # Subtraction of number  4  and  2  is :  2
    # Multiplication of number  4  and  2  is :  8
    # Division of number  4  and  2  is :  2.0

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 12>python Assignment12_3.py
    # Enter first number : 100
    # Enter second number : 50
    # Addition of number  100  and  50  is :  150
    # Subtraction of number  100  and  50  is :  50
    # Multiplication of number  100  and  50  is :  5000
    # Division of number  100  and  50  is :  2.0