class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Must be overwritten in subclasses")


class Cat(Animal):
    def talk(self):
        return "Meow!"


class Dog(Animal):
    def talk(self):
        return "Woof! Woof!"


class Cow(Animal):
    def talk(self):
        return "Moo! Moo!"
