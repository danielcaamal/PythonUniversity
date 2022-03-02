from Person import Person

class Employee(Person):
    def __init__(self, name, last_name, age, salary):
        super().__init__(name, last_name, age)
        self.salary = salary