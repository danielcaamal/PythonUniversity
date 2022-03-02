'''Class to instance object computers'''

from . Monitor import Monitor
from . Keyboard import Keyboard
from . Mouse import Mouse
import ast

class Computer():
    _id = 0
    
    @classmethod
    def counter_computers(cls):
        cls._id += 1
        return cls._id
    
    
    def __init__(self, name, monitor, keyboard, mouse):
        if not self._validate_computer(monitor, keyboard, mouse):
            raise Exception('Only type Monitor, Keyboard and Mouse can be added')
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse
        self._id_computer = self.counter_computers()
        
        
    # Getter and setter - name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    
    # Getter and setter - monitor
    @property
    def monitor(self):
        return self._monitor
    
    @name.setter
    def monitor(self, monitor):
        self._monitor = monitor
    
    
    # Getter and setter - keyboard
    @property
    def keyboard(self):
        return self._keyboard
    
    @keyboard.setter
    def keyboard(self, keyboard):
        self._keyboard = keyboard
    
    
    # Getter and setter - mouse
    @property
    def mouse(self):
        return self._mouse
    
    @keyboard.setter
    def mouse(self, mouse):
        self._mouse = mouse
        
    # Validations
    def _validate_computer(self, monitor, keyboard, mouse):
        if not isinstance(monitor, Monitor):
            return False
        if not isinstance(keyboard, Keyboard):
            return False
        if not isinstance(mouse, Mouse):
            return False
        return True
    
    
    # Override str method
    def __str__(self):
        return str({
            'id': self._id_computer,
            'name': self._name,
            'monitor': ast.literal_eval(str(self._monitor)),
            'keyboard': ast.literal_eval(str(self._keyboard)),
            'mouse': ast.literal_eval(str(self._mouse)),
        }) 