class Goat:
    age = 0         # class attributes
    name = ""       # class it is object type
    weight = 0.0

    def show(self): # self - mandatory, link for the object for what it was called
        print(self.name)
        print(self.age)

a = Goat()
a.name = "Notka"
a.age = 2
a.age += 1
b = Goat()
#b.name = "Zorka"
#b.age = 1
a.show()
b.show()


#####

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name, "+")
        # new attributes create only here

a = Student("Vasja", 17) # "Vasja", 17 - constructor parametrs
a.tail = "Fusica"
print(dir(a))