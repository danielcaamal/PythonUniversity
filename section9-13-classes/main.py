from Person import Person
from Employee import Employee

if __name__ == '__main__':
    
    print('Object Creation'.center(50,'-'))
    person1 = Person('Guillermo','Lopez', 25)
    
    print(person1)
    print(person1.name)
    
    person1.name = 'Rodolfo'
    print(person1.name)
    
    employee1 = Employee('Raul', 'Lara', 12, '5000')
    print(employee1.name)
    