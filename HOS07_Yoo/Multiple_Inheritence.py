class Animal:
    def sound(self):
        print("Animal makes a sound")


class Color:
    def show_color(self):
        print("This animal is brown")


class Dog(Animal, Color):
    def bark(self):
        print("Dog barks")


# 테스트
d = Dog()
d.sound()
d.show_color()
d.bark()
