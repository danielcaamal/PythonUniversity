import math
from decimal import Decimal

DASH = 50

def help_function():
    print(' 0. HELP FUNCTION '.center(DASH,'-'))
    help(int)
    help(str.capitalize)

def numerical_systems():
    print(' 1. NUMERICAL SYSTEMS '.center(DASH,'-'))

    # Decimal
    a = 10
    print(f'Decimal: {a}')

    # Binary
    b = 0b1010
    print(f'Binary: {b}')

    # Octal
    c = 0o12
    print(f'Octal: {c}')

    # Hexadecimal
    d = 0xA
    print(f'Hexadecimal: {d}')

def numeric_base_conversion():
    print(' 2. NUMERIC BASE CONVERSION '.center(DASH,'-'))

    # Convert int (with base 10)
    a = int('23',10)
    print(f'Base 10: {a}')

    # Convert int (with base 2)
    b = int('10111',2)
    print(f'Base 2: {a}')

    # Convert int (with base 8)
    c = int('27',8)
    print(f'Base 8: {c}')

    # Convert int (with base 16)
    d = int('17',16)
    print(f'Base 16: {d}')

def float_type():
    print(' 3. Float type '.center(DASH,'-'))

    # Formating floats
    a = 3.0
    print(f'Formating floats: {a:.3f}')

    # Exponential notation
    b = 3e-2
    c = 3e5
    print(f'Exponential notation: {b:.2f}, {c:.2f}')

    # Float conversions
    d = int(12) + float(13) # int + float => float
    print(f'Float conversions: {d:.2f}')

    # Infinity values
    e = float('inf') # Positive infinity
    f = float('-inf') # Negative infinity

    print(f'Positive infinity: {e}')
    print(f'Negative infinity: {f}')

    print(f'Is infinitive? {math.isinf(e)}')

    # Infinity using math
    g = math.inf
    print(f'Positive infinity (with math): {g}')
    h= -math.inf
    print(f'Negative infinity (with math): {h}')

    # Infinity using decimal
    i = Decimal('Infinity')
    print(f'Positive infinity (with decimal): {i}')
    j = -Decimal('Infinity')
    print(f'Negative infinity (with decimal): {j}')

    # Nan using float
    k = float('NaN') # Not is case-sensitive, Nan is an numerical undefined type
    print(f'NaN (using float): {k}')
    print(f'Is NaN? {math.isnan(k)}')

    # Nan using decimal
    l = Decimal('NaN') 
    print(f'NaN (using decimal): {l}')






    


if __name__ == '__main__':
    # Handling numerical types
    # help_function()
    numerical_systems()
    numeric_base_conversion()
    float_type()    