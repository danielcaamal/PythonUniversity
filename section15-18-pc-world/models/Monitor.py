'''Class to instance object Monitor: 
    - Create objects type Monitor
'''

class Monitor():
    _id = 0
    
    @classmethod
    def counter_monitors(cls):
        cls._id += 1
        return cls._id
    
    def __init__(self, brand, size):
        self._id_monitor = self.counter_monitors()
        self._brand = brand
        self._size = size
        
    # Getter and setter - monitor
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand
    
    # Getter and setter - keyboard
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
        
    def __str__(self):
        return str({
            'id': self._id_monitor,
            'brand': self._brand,
            'size': self._size
        })
    