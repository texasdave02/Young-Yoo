class Person:
    def displayData(self):
        print("I am a person")


class Employee(Person):
    def displayData(self):
        print("I am an employee")


p = Person()
e = Employee()

p.displayData()
e.displayData()
