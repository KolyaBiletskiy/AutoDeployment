


class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("Niko")

funny = Cat("Funny")


print(niko.speak())
print(funny.speak())



for pet in [niko, funny]:

    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(funny)



class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"


bagi = Dog("Bagi")
bobus = Cat("Bobus")


print(bagi.speak())
print(bobus.speak())


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello my name is", self.name)

class Enemy(Person):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def introduce(self):
        print("Hello my name is ", self.name)

Nick = Person('Nick')
Nick.introduce()

Enemy = Enemy("Enemy")
Enemy.introduce()



