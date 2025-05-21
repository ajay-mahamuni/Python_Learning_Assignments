#Assignment 5 - Problem 7- Area and Perimeter of a rectangle
        

def main():

    lenth = input("Enter length of a rectangle : ")    

    width = input("Enter width of a rectangle : ")    

    try:

        area = float(lenth) * float(width)

        perimeter = (float(lenth) + float(width)) * 2

        print("Area of rectangle is : ", area)

        print("Perimeter of rectangle is : ", perimeter)
        
    except ValueError:
        print("Enter valid length or width.")

if __name__ == "__main__":
    main()


    # Q7. Area and Perimeter of Rectangle
    # Accept the length and width of a rectangle. Calculate and display the area and perimeter.
    # Expected Input:
    # Enter length: 5
    # Enter width: 3
    # Expected Output:
    # Area: 15
    # Perimeter: 16

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_7.py
    # Enter length of a rectangle : 15
    # Enter width of a rectangle : 25
    # Area of rectangle is :  375.0
    # Perimeter of rectangle is :  80.0

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_7.py
    # Enter length of a rectangle : 400
    # Enter width of a rectangle : 200
    # Area of rectangle is :  80000.0
    # Perimeter of rectangle is :  1200.0

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_7.py
    # Enter length of a rectangle : 50
    # Enter width of a rectangle : asd
    # Enter valid length or width.