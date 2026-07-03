class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def bark(self):
        print("Dog Bark")


d = Dog()

d.sound()
d.bark()
