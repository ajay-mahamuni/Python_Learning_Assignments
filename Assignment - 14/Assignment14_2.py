#Assignment 14 - Problem 2 - Python OOP imlpementation using class and instance methods

class Rectancle:    

    def __init__(self,rLenght,rWidth):
        self.Lenght = rLenght
        self.Width = rWidth
        

    def Display(self):
        area = self.CalculateArea()
        perimeter = self.CalculatePerimeter()

        print("Area of reactanle is : ", area,end = " \n")
        print("Perimeter of reactanle is : ", perimeter,end = " \n\n")

    def CalculateArea(self):
        area = self.Lenght * self.Width
        return area
    
    def CalculatePerimeter(self):
        perimeter = (self.Lenght + self.Width) * 2
        return perimeter
        
def main():
    obj1 = Rectancle(50,30)
    obj2 = Rectancle(35,25)
    obj3 = Rectancle(12,60)
    
    obj1.Display()
    obj2.Display()
    obj3.Display()
    

if __name__ == "__main__":
    main()


    # 2. Write a class Rectangle with length and width. Add a method to compute area and
    # perimeter.
    # Area: 50, Perimeter: 30


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_2.py
    # Area of reactanle is :  1500
    # Perimeter of reactanle is :  160

    # Area of reactanle is :  875
    # Perimeter of reactanle is :  120

    # Area of reactanle is :  720
    # Perimeter of reactanle is :  144