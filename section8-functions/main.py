def my_function():



    print('Greetings from my function')
    




def names(*args):
    for arg in args:

        print(arg)
        


def names_dict(**kwargs):


    for key, value in kwargs.items():


        print(f'{key} - {value}')
        



def homework_10():



    '''Create a function that sums all the variable argument integers (args) received as paramaters of one function'''



    def add(*args):



        total = 0
        for arg in args:



            total += arg
        return total
            



    print(add(1,2,3,4,5,5))
    



def homework_11():



    '''Create a function that multiply all the variable argument integers (args) received as paramaters of one function'''


    def multiply(*args):



        total = 1
        for arg in args:
    


            total *= arg
        return total
            



    print(multiply(1,2,3,4,5,5))
    


def factorial(number):


    if number == 0:


        return 1
    else:


        return number*factorial(number-1)
    


def homework_12():
    


    def recursive(number):


        print(number)


        if number == 1:


            return number


        return recursive(number-1)



    recursive(3)



def homework_13():
    


    def calcular_total(pago_sin_impuesto,impuesto):


        return pago_sin_impuesto * (1 + impuesto / 100)
    


    pago_sin_impuesto = float(input('Ingresa el pago sin impuesto: '))


    impuesto = float(input('Ingresa el impuesto (0 - 100) %: '))
    


    print(calcular_total(pago_sin_impuesto, impuesto))
    



def homework_14():
    def celsius_fahrenheit(celsius):
        return celsius*9/5+32 

    def fahrenheit_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    celsius = float(input('Ingresa la temperatura en grados Celsius: '))
    fahrenheit = celsius_fahrenheit(celsius)
    print(f'La temperatura en grados Fahrenheit es: {fahrenheit}')
    
    
    fahrenheit = float(input('Ingresa la temperatura en grados Fahrenheit: '))
    celsius = fahrenheit_celsius(fahrenheit)
    print(f'La temperatura en grados Celsius es: {celsius}')
    




if __name__ == '__main__':



    my_function()
    



    names('Jose', 'Sarah', 'Laura')
    



    homework_10()
    


    homework_11()
    


    names_dict(IDE='Integrated Development Environment')
    


    print(factorial(5))
    


    # homework_12()
    


    # homework_13()
    
    homework_14()
    