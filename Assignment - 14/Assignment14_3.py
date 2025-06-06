#Assignment 14 - Problem 3 - Python OOP imlpementation using class and instance methods

class Book:    

    def __init__(self,bName,bPrice):
        self.Name = bName
        self.__Price = bPrice        

    def Display(self):
        print("Name of Book : ", self.Name,end=" \t")
        print("Price : ", self.__Price,end=" \t\n")

def main():

    obj1 = Book("The Time Machine",129)
    obj2 = Book("The Richest Man In Babylon",149)
    obj3 = Book("The Best of Sherlock Holmes",599)

    obj1.Display()
    obj2.Display()
    obj3.Display()
    

if __name__ == "__main__":
    main()



    # 3. Create a class Book with private attribute __price. Add methods to get and set the
    # price. Show encapsulation.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_3.py
    # Name of Book :  The Time Machine                Price :  129
    # Name of Book :  The Richest Man In Babylon      Price :  149
    # Name of Book :  The Best of Sherlock Holmes     Price :  599