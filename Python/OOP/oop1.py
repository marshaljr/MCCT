# OOP - Object Oriented Programming
# It is programming approach that uses objects and classes to structure code in a way that is modular, reusable, and easier to maintain.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine has started.")

    def stop_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine has stopped.")

car1 = Car("Toyota", "Camry", 2020)
car1.start_engine()
car1.stop_engine()
car2 = Car("Honda", "Civic", 2021)
car2.start_engine()
car2.stop_engine()

#class --> A class is a blueprint for creating objects. It defines the attributes and methods that the objects created from the class will have.
#object --> An object is an instance of a class. It is created from the class and has its own unique state and behavior.
#Attributes --> Attributes are the data stored in an object. They represent the state of the object and can be accessed and modified using dot notation.
#Methods --> Methods are functions that are defined within a class and can be called on objects of that class. They define the behavior of the objects.
#Constructor --> A constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object.

#self --> The self parameter is a reference to the current instance of the class. It is used to access the attributes and methods of the object.
