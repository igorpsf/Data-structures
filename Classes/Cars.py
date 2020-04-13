class Car:

    def __init__(self, model, color, range):
        self.model = model
        self.color = color
        self.range = range

    def model_type(self):
        print("Car model " + self.model)

c1 = Car("Model S", "Black", 390)
#c1.model = "Model S"
#c1.color = "Black"
#c1.range = 390

c2 = Car("Model 3", "Red", 322)
#c2.model = "Model 3"
#c2.color = "Red"
#c2.range = 322

c3 = Car("Model X", "Grey", 351)
#c3.model = "Model X"
#c3.color = "Grey"
#c3.range = 351

c4 = Car("Model Y", "Red", 315)
#c4.model = "Model Y"
#c4.color = "Red"
#c4.range = 315

#c1.model_type()
#c2.model_type()


###############

class Person:

    def __init__(self, name, job, happiness):
        self.name = name
        self.job = job
        self.happiness = happiness


    def set_happy(self):
        self.happiness = True

    def set_sad(self):
        self.happiness = False

p1 = Person("Igor", "Google", True)
p2 = Person("Neha", "Facebook", True)
p3 = Person("Dima", "8x8", False)

p1.car_own = c3
p2.car_own = c1
p3.car_own = c2

p1.car_own.model_type()
p2.car_own.model_type()
p3.car_own.model_type()