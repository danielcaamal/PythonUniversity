'''Class to instance object InputDevice: 
    - Create objects type InputDevice
'''

class InputDevice():
    def __init__(self, input_type, brand):
        self._input_type = input_type
        self._brand = brand
    
    # Getter and setter - input_type
    @property
    def input_type(self):
        return self._input_type
    
    @input_type.setter
    def input_type(self, input_type):
        self._input_type = input_type
    
    # Getter and setter - brand
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand
    
    
    def __str__(self):
        return str({
            'brand': str(self.brand),
            'input_type': str(self.input_type)
        })