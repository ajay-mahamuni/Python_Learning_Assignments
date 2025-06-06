#Assignment 14 - Problem 8 - Python OOP imlpementation using class and instance methods

class Vehicle:    

    def __init__(self,vMake,vModel,vFuelType):
        self.Make = vMake
        self.Model = vModel
        self.FuelType = vFuelType
        print("Inside Vehicle constructor..")

        print("Make : ", self.Make,end=" \t")
        print("Model : ", self.Model,end=" \t")
        print("Fuel Type : ", self.FuelType,end=" \t\n")

    def Start(self):
        print("Start method in Vehicle..")
        

    
        

class Car(Vehicle):
    def __init__(self,cMake,cModel,cFuelType,cTransmission,cSafetyRating,cAirBags):

        print("Inside Car's constructor..")

        super().__init__(cMake,cModel,cFuelType)

        self.Transmission = cTransmission
        self.SafetyRating = cSafetyRating
        self.AirBags = cAirBags
        

    def Start(self):
        print("Start method in Car..")
        print("Transmission : ", self.Transmission,end=" \t")
        print("SafetyRating : ", self.SafetyRating,end=" \t")
        print("AirBags : ", self.AirBags,end=" \t\n\n")
        
        

def main():
    obj1 = Car("Tata","Nexon","Petrol","Automatic",4.5,6)
    obj1.Start()

if __name__ == "__main__":
    main()



    # 8. Create a class Vehicle with method start(). Derive class Car and override the
    # method start() with additional behavior. Show method overriding.


    # D:\ajay.mahamuni\Python-2025\Programs\Python_Learning_Assignments\Assignment - 14>python Assignment14_8.py
    # Inside Car's constructor..
    # Inside Vehicle constructor..
    # Make :  Tata    Model :  Nexon  Fuel Type :  Petrol
    # Start method in Car..
    # Transmission :  Automatic       SafetyRating :  4.5     AirBags :  6