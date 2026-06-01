programmer = {
    "name": "Gopal",
    "age": 21,
    "phone": 1234567890
}

class Duck:
    def quack(self):
        print("Quack Quack")

    def fly(self):
        print("Flap Flap")

class Person:

    def quack(self):
        print("I'm quacking like a duck")

    def fly(self):
        print("I'm Flaping my arms")

def quack_and_fly(thing):
    print()
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as err:
        print(err)
    finally:
        print()

d = Duck()
p = Person()

quack_and_fly(d)
quack_and_fly(p)

try:
    print("Name:{name}\nAge:{age}\nPhone:{phone}\n".format(**programmer))
except TypeError as err:
    print(err)