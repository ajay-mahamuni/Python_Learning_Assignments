#Assignment 5 - Problem 6- Conver degree celcius to degree fahrenheit
        

def main():

    number = input("Enter temperature in Celsius : ")    

    try:        
        result = (float(number) * 9/5) + 32
        print("Temperature in Fahrenheit : ", result,"°F")
        
    except ValueError:
        print("Enter valid temperature.")

if __name__ == "__main__":
    main()


    # Q6. Celsius to Fahrenheit Converter
    # Accept temperature in Celsius and convert it to Fahrenheit using the formula:
    # F = (C × 9/5) + 32
    # Expected Input:
    # Enter temperature in Celsius: 25
    # Expected Output:
    # Temperature in Fahrenheit: 77.0°F


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_6.py
    # Enter temperature in Celsius : ads
    # Enter valid temperature.

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_6.py
    # Enter temperature in Celsius : 45
    # Temperature in Fahrenheit :  113.0 °F

    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 5>python Assignment5_6.py
    # Enter temperature in Celsius : 12.5
    # Temperature in Fahrenheit :  54.5 °F