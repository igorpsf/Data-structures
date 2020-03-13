class Goat:
    age = 0
    name = ""
    weight = 0.0

    def show(self):
        print(self.name)
        print(self.age)

a = Goat()
a.name = "Notka"
a.age = 2
a.age += 1
b = Goat()
b.name = "Zorka"
b.age = 1
a.show()
b.show()