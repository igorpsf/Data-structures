
class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.color.upper())
print(jonagold.flavor)


###

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Igor")
# Call the greeting method
print(some_person.greeting())


###

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

anton = Apple("red", "sweet")
print(anton) # Will print because of __str__ method
help(Apple)
