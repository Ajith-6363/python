class circle:
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*(self.radius)**2
ob=circle(5)
print(ob.circumference())
print(ob.area())
        