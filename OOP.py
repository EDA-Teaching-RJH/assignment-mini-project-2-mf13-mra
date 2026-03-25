class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"hello my name is {self.name}")
    

class student(person):
    def __init__(self, name, age, graduationyear):
        super().__init__(name, age)
        self.graduationyear = graduationyear

        def sayGraduation(self):
            print(f"hello i graduate in {self.graduationyear} and my name is {self.name}")
            


        