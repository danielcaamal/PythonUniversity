

class Person():
    def __init__(self, name, last_name,age):
        self._name = name
        self._last_name = last_name
        self._age = age
    
    @property  
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
    
    # Only read    
    @property
    def age(self):
        return self._age
    
    # @age.setter
    # def age(self, age):
    #     self._age = age
    
    
    def __del__(self):
        pass
    
    def __str__(self):
        return f'''{self._name} {self._last_name} - {self._age}'''