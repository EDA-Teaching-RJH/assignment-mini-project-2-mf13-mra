#program to show basic OOP functionality in python
class person():
    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age
    
    def greet(self): #basic functionalityshared across all people and its subclasses
        print(f"hello my name is {self.name}")
    
#subclass from person
class student(person):
    def __init__(self, name, age, graduationyear):
        super().__init__(name, age) #constructor from super class
        self.graduationyear = graduationyear

        def sayGraduation(self):
            print(f"hello i graduate in {self.graduationyear} and my name is {self.name}")



            


        