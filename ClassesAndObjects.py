class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()

###

class Person:
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned

    def sitDown(self):
        self.isSitting = True

    def standUp(self):
        self.isSitting = False

p1 = Person("Alice", "aggressiove", False, r2)
p2 = Person("Becky", "talkative", True, r1)

# p1.robotOwned = r2
# p2.robotOwned = r1

p1.robotOwned.introduce_self()
p2.robotOwned.introduce_self()


