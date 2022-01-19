'''Class to instance object orders: 
    - Create objects type Order
    - Save list of the object Computer
'''

from . Computer import Computer

class Order():
    _id = 0
    _computers = []
    
    @classmethod
    def counter_order(cls):
        cls._id += 1
        return cls._id
    
    def __init__(self, computers):
        for computer in computers:
            if not self._validate_computer(computer):
                raise Exception('Only computers can be added to the order')
            self.add_computer(computer)
        self._id_order = self.counter_order()
        
    def add_computer(self, computer):
        self._computers.append(computer)
        
    def _validate_computer(self, computer):
        if isinstance(computer, Computer):
            return True
        return False
    
    def __str__(self):
        arr = ''
        for computer in self._computers:
            arr += f'{computer} '
        return f'Order({self._id_order}) [ {arr} ]'