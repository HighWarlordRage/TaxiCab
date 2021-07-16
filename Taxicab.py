#Title: Project-5b
class Taxicab:
    """class named Taxicab that has three private data members
     one that holds the current x-coordinate
     one that holds the current y-coordinate
     one that holds the current odometer reading"""
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.odometer = 0

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_odometer(self):
        return self.odometer

    def move_x(self, x):
        self.x_coord = self.x_coord + x
        self.odometer = self.odometer + abs(x)

    def move_y(self, y):
        self.y_coord = self.y_coord + y
        self.odometer = self.odometer + abs(y)

#cab = Taxicab(5, -8)        # creates a Taxicab object at coordinates (5, -8)
#cab.move_x(3)               # moves cab 3 units "right"
#cab.move_y(-4)              # moves cab 4 units "down"
#cab.move_x(-1)              # moves cab 1 unit "left"
#print(cab.get_odometer())   # prints the current odometer reading
