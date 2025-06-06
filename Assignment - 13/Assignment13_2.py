#Assignment 13 - Problem 2 - Python OOP imlpementation using class and instance methods

class BankAccount:

    ROI = 10.5

    def __init__(self):        
        self.Name = input("Enter a name : ")
        self.Amount =   float(input("Enter an amount : "))


    def Display(self):
        print("Name : ", self.Name, end=" ")
        print("| Account Balance : ", self.Amount, end=" \n")

    def Deposit(self):
        depAmount = float(input("Enter amount to deposit : "))

        self.Amount = self.Amount + depAmount

    def Withdraw(self):
        witAmount = float(input("Enter amount to withdraw : "))

        self.Amount = self.Amount - witAmount

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest on amount ", self.Amount, " is : ", interest)
        
def main():
    
    Obj1 = BankAccount()
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Display()
    Obj1.Withdraw()
    Obj1.Display()
    Obj1.CalculateInterest()

    Obj2 = BankAccount()
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Display()
    Obj2.Withdraw()
    Obj2.Display()
    Obj2.CalculateInterest()

    Obj3 = BankAccount()
    Obj3.Display()
    Obj3.Deposit()
    Obj3.Display()
    Obj3.Withdraw()
    Obj3.Display()
    Obj3.CalculateInterest()

if __name__ == "__main__":
    main()


    # 2. Write a program which contains one class named as BankAccount.
    # BankAccount class contains two instance variables as Name & Amount.
    # That class contains one class variable as ROI which is initialise to 10.5.
    # Inside init method initialise all name and amount variables by accepting the values from user.
    # There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
    # CalculateIntrest().
    # Deposit() method will accept the amount from user and add that value in class instance variable
    # Amount.
    # Withdraw() method will accept amount to be withdrawn from user and subtract that amount
    # from class instance variable Amount.
    # CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
    # which is Class variable as ROI.
    # And Display() method will display value of all the instance variables as Name and Amount.
    # After designing the above class call all instance methods by creating multiple objects.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 13>python Assignment13_2.py
    # Enter a name : Ajay
    # Enter an amount : 6000
    # Name :  Ajay | Account Balance :  6000.0
    # Enter amount to deposit : 5000
    # Name :  Ajay | Account Balance :  11000.0
    # Enter amount to withdraw : 300
    # Name :  Ajay | Account Balance :  10700.0
    # Interest on amount  10700.0  is :  1123.5
    # Enter a name : Mayuri
    # Enter an amount : 8000
    # Name :  Mayuri | Account Balance :  8000.0
    # Enter amount to deposit : 2000
    # Name :  Mayuri | Account Balance :  10000.0
    # Enter amount to withdraw : 5000
    # Name :  Mayuri | Account Balance :  5000.0
    # Interest on amount  5000.0  is :  525.0
    # Enter a name : Amey
    # Enter an amount : 5250
    # Name :  Amey | Account Balance :  5250.0
    # Enter amount to deposit : 1850
    # Name :  Amey | Account Balance :  7100.0
    # Enter amount to withdraw : 500
    # Name :  Amey | Account Balance :  6600.0
    # Interest on amount  6600.0  is :  693.0