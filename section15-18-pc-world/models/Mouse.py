'''Class to instance object Mouse: 
    - Create objects type Mouse
'''

from . InputDevice import InputDevice
import ast
class Mouse(InputDevice):
    _id = 0
    
    @classmethod
    def counter_mouse(cls):
        cls._id += 1
        return cls._id
    
    def __init__(self, input_type, brand):
        InputDevice.__init__(self, input_type, brand)
        self._id_mouse = self.counter_mouse()
        
    def __str__(self):
        return str({
            'id': self._id,
            'input_device': ast.literal_eval(InputDevice.__str__(self))
        })