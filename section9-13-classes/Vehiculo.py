

class Vehiculo():
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas
    def __str__(self):
        return f'Vehiculo( color:{self._color}, ruedas: {self._ruedas} )'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    def __str__(self):
        return f'Coche( color:{self._color}, ruedas: {self._ruedas}, velocidad: {self._velocidad} km/hr )'
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo
    def __str__(self):
        return f'Bicicleta( color:{self._color}, ruedas: {self._ruedas}, tipo: {self._tipo} )'
    

print(Vehiculo('Azul', 4))

print(Coche('Azul', 4, 180))

print(Bicicleta('Roja', 2, 'Urbana'))
