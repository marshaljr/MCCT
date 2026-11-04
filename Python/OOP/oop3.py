class Student:
    def __init__(self, name, age, phone):
        self.name = name
        self._age = age
        self.__phone = phone

    def get_age(self): #getter method for age
        return self._age

    def set_phone(self, new_phone): #setter method for phone
        self.__phone = new_phone
        return new_phone
    
    def get_phone(self): #getter method for phone
        return self.__phone


sdt1 = Student("Alice", 20, "123-456-7890")
print(sdt1.name)  # Output: Alice
print(sdt1.get_age())  # Output: 20
print(sdt1.get_phone())  # Output: 123-456-7890
print(sdt1.set_phone("098-765-4321"))  # Update phone number