#Assignment 13 - Problem 1 - Python OOP imlpementation using class and instance methods

class BookStore:

    NumOfBooks = 0

    def __init__(self,bName,bAuthor):
        self.Name = bName
        self.Author = bAuthor
        BookStore.NumOfBooks = BookStore.NumOfBooks + 1


    def Display(self):
        print(self.Name, end=" ")
        print(self.Author, end=" ")
        print("Number of books : ", BookStore.NumOfBooks)    

def main():
    
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()

    Obj3 = BookStore("Malgudi Days", "R.K. Narayan")
    Obj3.Display()
    
    

if __name__ == "__main__":
    main()


    # 1.Write a program which contains one class named as BookStore.
    # BookStore class contains two instance variables as Name ,Author.
    # That class contains one class variable as NoOfBooks which is initialise to 0.
    # There is one instance methods of class as Display which displays name , Author and number of
    # books.
    # Initialise instance variable in init method by accepting the values from user as name and author.
    # Inside init method increment value of NoOfBooks by one.
    # After creating the class create the two objects of BookStore class as
    # Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
    # Obj1.Display() # Linux System Programming by Robert Love. No of books : 1
    # Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
    # Obj2.Display()


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 13>python Assignment13_1.py
    # Linux System Programming Robert Love Number of books :  1
    # C Programming Dennis Ritchie Number of books :  2

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 13>python Assignment13_1.py
    # Linux System Programming Robert Love Number of books :  1
    # C Programming Dennis Ritchie Number of books :  2
    # Malgudi Days R.K. Narayan Number of books :  3