#Assignment 14 - Problem 9 - Python OOP imlpementation using class and instance methods

class Product:    

    def __init__(self,pName,pPrice):
        self.Name = pName
        self.Price = pPrice
        print("Product : ",self.Name,end=" ")
        print("Price : ",self.Price, end=" \n")

    def __eq__(self, otherProduct):
        if self.Price == otherProduct.Price:
            return True
        else:
            return False
        
def Display(obj1,obj2):
    response = obj1.__eq__(obj2)

    if response:
        print("Product prices are equal")
    else:
        print("Product prices are not equal")

        

def main():
    obj1 = Product("Dell Keyboard",2100)
    obj2 = Product("iBall Keyboard",1700)

    Display(obj1,obj2)

    obj1 = Product("Dell Mouse",1200)
    obj2 = Product("iBall Mouse",1200)

    Display(obj1,obj2)

    

if __name__ == "__main__":
    main()



    # 9. Create a class Product with attributes name and price. Implement __eq__ method
    # to compare two products if they are equal in price.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_9.py
    # Product :  Dell Keyboard Price :  2100
    # Product :  iBall Keyboard Price :  1700
    # Product prices are not equal
    # Product :  Dell Mouse Price :  1200
    # Product :  iBall Mouse Price :  1200
    # Product prices are equal