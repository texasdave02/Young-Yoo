class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Pug(Dog):
    def speak(self):
        print("Pug makes a cute bark")


# 테스트
a = Animal()
d = Dog()
p = Pug()

a.speak()
d.speak()
p.speak()
