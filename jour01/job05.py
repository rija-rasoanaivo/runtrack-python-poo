class Point():

    def __init__(self, x, y):
        """Initialize the value of x and y."""
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        """Print the value of x and y."""
        print("x = " + str(self.x) + " y = " + str(self.y))

    def afficherX(self):
        """Print the value of x."""
        print("x = " + str(self.x))

    def afficherY(self):
        print("y = " + str(self.y))

    def changerX(self, x):
        """Change the value of x."""
        self.x = x

    def changerY(self, y):
        """Change the value of y."""
        self.y = y

point_attribue = Point(2, 3)

point_attribue.afficherLesPoints()
point_attribue.afficherX()
point_attribue.afficherY()
point_attribue.changerX(5)
point_attribue.changerY(7)
point_attribue.afficherLesPoints()