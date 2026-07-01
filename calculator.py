class calculator:
    def __init__(self, a,b):
        self.a=a
        self.b=b
        self.result = 0



    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
object1 = calculator(10, 5)
multiplication_result = object1.multiply(object1.a, object1.b)
print(f"Multiplication Result: {multiplication_result}")