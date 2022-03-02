


def arithmetic_operators():

    # Arithmetic Operators


    var1 = 7

    var2 = 2


    add = var1 + var2

    print(f'Result add: {add}')


    minus = var1 - var2

    print(f'Result substract: {minus}')


    mul = var1 * var2

    print(f'Result multiplication: {mul}')


    div = var1 / var2

    print(f'Result division: {div}')


    div_trunc = var1 // var2

    print(f'Result division truncated: {div_trunc}')


    mod = var1 % var2

    print(f'Result module: {mod}')


    exp = var1 ** var2

    print(f'Result exponential: {exp}')
    

def assignment_operators():

    # Assignment operators

    myVar = 10

    myVar += 1

    print(myVar)


def homework_3():

    # Homework #3

    height = int(input('Proporciona el alto: '))

    width = int(input('Proporciona el ancho: '))


    area = height * width

    perimeter = (height + width) * 2

    print(f'''

        Area: {area}

        Perimeter: {perimeter}      
    ''')
    
def relational_operators():

    a = 2

    b = 3

    print(f'Result == : {a==b}')

    print(f'Result != : {a!=b}')

    print(f'Result >  : {a>b}')

    print(f'Result <  : {a<b}')

    print(f'Result >= : {a>=b}')

    print(f'Result <= : {a<=b}')
    
def is_even(number):
    if number % 2 == 0:
        return True
    return False

def homework_4():
    number1 = int(input('Proporciona el numero 1: '))
    number2 = int(input('Proporciona el numero 2: '))
    print(f'EL numero mayor es: {number1 if number1 > number2 else number2}')
    

if __name__ == "__main__":

    # arithmetic_operators()

    # homework_3()

    # assignment_operators()
    
    # relational_operators()
    
    # print('Is even: ',is_even(3))
    
    homework_4()