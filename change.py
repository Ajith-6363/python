# the way to change the class variable is by using the class name and not the object name
class change:
    name="ajith"
    def __init__(self,age):
        self.age=age
    @staticmethod
    def greet(self):
        print(f"Hello {self.name}, your age is {self.age}")
object1=change(25)
change.name="amar"
# this will change the name for the class variable, affecting all instances

object1.greet(self=object1)  # Output: Hello amar, your age is 25
object2=change(30)
object2.greet(self=object2)  # Output: Hello amar, your age is 30