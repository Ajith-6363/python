class Employee:
    def __init__(self, name, salary, increment=0.0):
        self.name = name
        self._salary = salary
        self._increment = increment

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if value < 0:
            raise ValueError("Increment cannot be negative")
        self._increment = value

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary_after_increment):
        if new_salary_after_increment <= self.salary:
            raise ValueError("New salary after increment must be greater than current salary")
        self.increment = ((new_salary_after_increment / self.salary) - 1) * 100

    def addsalary(self, amount):
        self.salary += amount

obj = Employee("ajith", 50000, 3.5)
print(obj.salaryAfterIncrement)
    