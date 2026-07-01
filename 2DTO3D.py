# Practice Set
# CHAPTER 11
# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"2D Vector: ({self.x}, {self.y})")

class Vector3D(Vector2D):
    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"3D Vector: ({self.x}, {self.y}, {self.z})")
a1 = Vector2D(3, 4)
a1.display()
a2 = Vector3D(43.5, 44.5, 45.5)
a2.display()