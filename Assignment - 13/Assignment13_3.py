#Assignment 13 - Problem 3 - Python OOP imlpementation using class and instance methods

class Arithmetic:
    def __init__(self):
        self.Value = input("Enter a number : ")

        if self.Value.isdigit():
            self.Value = int(self.Value)
        else:
            print("Enter a valid number.")

    def ChkPrime(self):        

        flag = True

        if self.Value == 0 or self.Value == 1:
            flag = False            
        elif self.Value > 1:
            for num in range(2,self.Value):
                if (self.Value % num) == 0:
                    flag = False
                    break
        
        if flag: 
            print("Entered number ", self.Value, " is a Prime number.")
        else:
            print("Entered number ", self.Value, " is NOT a Prime number.")


    def ChkPerfect(self):
        sumFactor = self.SumFactors()

        if self.Value == sumFactor:
            print("Entered number ",self.Value, " is a PERFECT number.")
        else:
            print("Entered number ",self.Value, " is NOT a PERFECT number.")

        

    def SumFactors(self):
        sumFactor = 0
        factorList = self.Factors()

        for i in factorList:
            sumFactor = sumFactor + i

        print("Sum of Factors of number ",self.Value, " is : ",sumFactor)

        return sumFactor

    def Factors(self):
        dataList = []

        for num in range(1,self.Value):
            if self.Value % num == 0:
                dataList.append(num)


        print("Factors of number ",self.Value, " are : ",dataList)

        return dataList
        

        
def main():
    obj1 = Arithmetic()
    obj1.ChkPrime()
    obj1.ChkPerfect()
    
    
if __name__ == "__main__":
    main()


    # 3. Write a program which contains one class named as Numbers.
    # Arithmetic class contains one instance variables as Value.
    # Inside init method initialise that instance variables to the value which is accepted from user.
    # There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
    # Factors().
    # ChkPrime() method will returns true if number is prime otherwise return false.
    # ChkPerfect() method will returns true if number is perfect otherwise return false.
    # Factors() method will display all factors of instance variable.
    # SumFactors() method will return addition of all factors. Use this method in any another method
    # as a helper method if required.
    # After designing the above class call all instance methods by creating multiple objects.



    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 13>python Assignment13_3.py
    # Enter a number : 6
    # Entered number  6  is NOT a Prime number.
    # Factors of number  6  are :  [1, 2, 3]
    # Sum of Factors of number  6  is :  6
    # Entered number  6  is a PERFECT number.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 13>python Assignment13_3.py
    # Enter a number : 12
    # Entered number  12  is NOT a Prime number.
    # Factors of number  12  are :  [1, 2, 3, 4, 6]
    # Sum of Factors of number  12  is :  16
    # Entered number  12  is NOT a PERFECT number.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 13>python Assignment13_3.py
    # Enter a number : 171
    # Entered number  171  is NOT a Prime number.
    # Factors of number  171  are :  [1, 3, 9, 19, 57]
    # Sum of Factors of number  171  is :  89
    # Entered number  171  is NOT a PERFECT number.