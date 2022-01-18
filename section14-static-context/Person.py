

class Person():
    _id = 0
    
    @classmethod
    def generate_next_id(cls):
        cls._id += 1
        return cls._id
    
    def __init__(self, name, age):
        self.id_person = Person.generate_next_id()
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'Person [{self.id_person} {self.name} {self.age}]'