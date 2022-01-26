DASH = 50

def bool_type():
    print(' 1. Bool type '.center(DASH,'-')) 

    # Numerical types: False for 0, else True 
    print('Numerical types')
    a = bool(0)
    print(f'Result: {a}')
    b = bool(0.00)
    print(f'Result: {b}')
    c = bool(5)
    print(f'Result: {c}')
    d = bool(12.0)
    print(f'Result: {d}')

    # String types: False for '', else True 
    print('String types')
    e = bool('')
    print(f'Result: {e}')
    f = bool('0')
    print(f'Result: {f}')

    # Collection types: False for (),{},[], else True
    print('Collection types')
    
    # List
    g = bool([])
    print(f'Result: {g}')
    h = bool(['1', '2'])
    print(f'Result: {h}')

    # Tuple
    i = bool(('1', '2'))
    print(f'Result: {i}')

    # Dictionary, sets
    j = bool({})
    print(f'Result: {j}')

    # Control Statements
    if []:
        print('This are not going to be executed')
    else:
        print('Printing this')


if __name__ == '__main__':
    # Handling booleans
    bool_type()