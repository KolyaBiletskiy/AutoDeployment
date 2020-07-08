class Inherited():
    def a(self):
        # call base method here
        print("Inherited_a")

class Base(Inherited):
    def a(self):
        print("Base_a")

obj = Base()

obj.a()


class Animall():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

Animall()


class Dog(Animall):
    def __init__(self):
        Animall.__init__(self)

Dog().who_am_i()


class Base:
    def a(self):
        print("Base_a")

class Inherited(Base):
    def a(self):
        # Base.__init__(self)
        # Base.a(self)
        # call base method here
        print("Inherited_a")

obj = Inherited()

obj.a()

Base.a(obj)



