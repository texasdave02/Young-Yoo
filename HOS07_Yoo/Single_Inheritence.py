class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


# 테스트
a = Animal()
d = Dog()

a.speak()
d.speak()
