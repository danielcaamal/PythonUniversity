from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, height, width):
        if not self._validate(height) or not self._validate(width):
            raise Exception('Incorrect value')
        self._height = height
        self._width = width
    
    def __str__(self):
        return f'''
            Figure : 
                height: {self._height},
                width: {self._width},
        '''
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = width

    def _validate(self, value):
        return Exception('Invalid error') if value > 0 else None
    
    @abstractmethod    
    def area(self):
        pass

    
class Color():
    def __init__(self, color):
        self._color = color
    
    def __str__(self):
        return f'''
            Color:
                color: {self._color}
        '''
        
    @property
    def color(self):
        return self.color
    
    @color.setter
    def color(self, color):
        self._color = color



class Square(Figure, Color):
    def __init__(self, height, width, color):
        Square.__init__(self, height, width)
        Color.__init__(self, color)
        
    def __str__(self):
        return f'''
            Square : 
                height: {self._height},
                width: {self._width},
                color: {self._color},
                area: {self.area()}
        '''
        
    def area(self):
        return float(self._height) * float(self._width)
    

class Triangle(Figure, Color):
    def __init__(self, height, width, color):
        Figure.__init__(self, height, width)
        Color.__init__(self, color)
        
    def __str__(self):
        return f'''
            Triangle : 
                height: {self._height},
                width: {self._width},
                color: {self._color},
                area: {self.area()}
        '''
        
    def area(self):
        return float(self._height) * float(self._width) / 2

