# Create a class “Programmer” for storing information of few programmers working at
# Microsoft. Store Name, Age, Salary, Programming Languages known (Python / Java / C++ / JavaScript) and write a method to display the information of few programmers.
class Programmer:
    def __init__(self, name, age, salary, languages):
        self.name = name
        self.age = age
        self.salary = salary
        self.languages = languages

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary}")
        print(f"Programming Languages Known: {', '.join(self.languages)}")
object1 = Programmer("Ajith", 25, 50000, ["Python", "Java"])
object2 = Programmer("Amar", 30, 60000, ["C++", "JavaScript"])
object1.display_info()
object2.display_info()