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
            print(f"hello i graduate in {self.graduationyear} and my name is {self.name}!")

#another subclass
class teacher(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def calculateYearlySalary(self):
        yearlySalary = self.salary * 12
        return yearlySalary
    
    def teach(self, student : student): #2 different subclasses interacting with eachother!
        print(f"hello I am {self.name}, and today I will teach {student.name} about something cool!")

student1 = student("Shalissa", 18, 2030)

teacher1 = teacher("Mr.Tank", 27, 1500)

student1.sayGraduation()
student1.greet()

#student1.calculateYearlySalary() would return an error because teacher is a different subclass :0
#just like the teacher1.saysGraduation() would return an error

teacher1.greet()
print(f"I make {teacher1.calculateYearlySalary()} a year!")

del student1 #you can delete them too
#doing anything with the student1 object would cause error because non-existent

