
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def get_current(self):
        return self.current

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current = self.current + 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current = self.current - 1

    def go_to(self, current):
        """Makes the elevator go to the specific floor."""
        self.current = current

    #self.floor = floor
    #self.current = self.floor
    #return self.current
    # self.floor

    def __str__(self):
        return "Elevator is in {}".format(self.current)


elevator = Elevator(-1, 10, 0)

elevator.up()
print(elevator.current)     # 1

elevator.down()
print(elevator.current)     # 0

elevator.go_to(10)
print(elevator.current)   # 10
