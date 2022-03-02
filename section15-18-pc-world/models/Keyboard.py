'''Class to instance object Keyboard: 
    - Create objects type Keyboard
'''

from . InputDevice import InputDevice
import ast

class Keyboard(InputDevice):
    _id = 0
    
    @classmethod
    def counter_keyboards(cls):
        cls._id += 1
        return cls._id
    
    def __init__(self, input_type, brand):
        InputDevice.__init__(self, input_type, brand)
        self._id_keyboard = self.counter_keyboards()
        
    def __str__(self):
        return str({
            'id': self._id_keyboard,
            'input_device': ast.literal_eval(InputDevice.__str__(self))
        })
    