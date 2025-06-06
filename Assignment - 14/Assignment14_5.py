#Assignment 14 - Problem 5 - Python OOP imlpementation using class and instance methods

class BankAccount:
    
    def __init__(self):        
        self.Name = input("Enter a name : ")
        self.AccountNumber = input("Enter account number : ")
        self.AccountBalance =   float(input("Enter account balance : "))


    def Display(self):
        print("Name : ", self.Name, end=" \t")
        print("Account Number : ", self.AccountNumber, end=" \t")
        print("| Account Balance : ", self.AccountBalance, end=" \t\n")

    def Deposit(self):
        depAmount = float(input("Enter amount to deposit : "))

        self.AccountBalance = self.AccountBalance + depAmount

    def Withdraw(self):
        witAmount = float(input("Enter amount to withdraw : "))

        self.AccountBalance = self.AccountBalance - witAmount

    
        
def main():
    
    Obj1 = BankAccount()
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Display()
    Obj1.Withdraw()
    Obj1.Display()

    print(end="\n")
    
    Obj2 = BankAccount()
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Display()
    Obj2.Withdraw()
    Obj2.Display()

    print(end="\n")
    
    Obj3 = BankAccount()
    Obj3.Display()
    Obj3.Deposit()
    Obj3.Display()
    Obj3.Withdraw()
    Obj3.Display()
    
if __name__ == "__main__":
    main()



    # 5. Create a class BankAccount with account_number, name, and balance. Use
    # __init__ and create methods for deposit, withdraw, and displaying balance.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_5.py
    # Enter a name : Ajay
    # Enter account number : 1011001
    # Enter account balance : 52000
    # Name :  Ajay    Account Number :  1011001       | Account Balance :  52000.0
    # Enter amount to deposit : 7000
    # Name :  Ajay    Account Number :  1011001       | Account Balance :  59000.0
    # Enter amount to withdraw : 5000
    # Name :  Ajay    Account Number :  1011001       | Account Balance :  54000.0

    # Enter a name : Mayuri
    # Enter account number : 1011002
    # Enter account balance : 87000
    # Name :  Mayuri  Account Number :  1011002       | Account Balance :  87000.0
    # Enter amount to deposit : 7850
    # Name :  Mayuri  Account Number :  1011002       | Account Balance :  94850.0
    # Enter amount to withdraw : 52650
    # Name :  Mayuri  Account Number :  1011002       | Account Balance :  42200.0

    # Enter a name : Amey
    # Enter account number : 1011003
    # Enter account balance : 35000
    # Name :  Amey    Account Number :  1011003       | Account Balance :  35000.0
    # Enter amount to deposit : 2500
    # Name :  Amey    Account Number :  1011003       | Account Balance :  37500.0
    # Enter amount to withdraw : 500
    # Name :  Amey    Account Number :  1011003       | Account Balance :  37000.0