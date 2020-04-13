### Inheritance

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)


### Inheritance 2

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
    sound =  "Oink!"

class Cow(Animal):
    sound = "Mooooo"

hamlet = Piglet("Hamlet")
hamlet.speak()  # Oink! I'm Hamlet! Oink!

milky = Cow("Milky White")
milky.speak()   # Mooooo I'm Milky White! Mooooo

### Inheritance 3 (Composition) : Let’s create a new class together and inherit from it. Below we have a base class called Clothing. Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks to make it work properly.

class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()

