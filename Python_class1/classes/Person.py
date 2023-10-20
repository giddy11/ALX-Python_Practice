class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("{} is Talking.....".format(self.name))

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat:
    def walk(self):
        print("walk")


test = Person("Gideon")
dog = Dog()
cat = Cat()


test.talk()