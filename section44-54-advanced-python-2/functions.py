import keyword
DASH = 50

def nested_functions():
    print(' 1. Nested Functions '.center(DASH,'-'))
    
    # Nested functions
    def calculator(a,b, operation='+'):
        # 1. Define the function
        def add(a, b):
            return a + b

        def sub(a, b):
            return a - b
        
        # 2. Call the function
        if operation == '+':
            return add(a,b)
        elif operation == '-':
            return sub(a,b)
        else:
            return None
    
    print(f'Nested function: {calculator(5, 10, "+")}')


var_global = 'GLOBAL'
counter = 0


def scopes():
    print(' 2. Scopes '.center(DASH,'-'))

    print(f'Global variable: {var_global}')

    def _print():
        global var_global           # We need to add this to wrote the function (1)

        print(f'Global variable since function: {var_global}')

        var_local = 'LOCAL'         # If we want to wrote this functions inside the nested function we need to declare nonlocal (2)
        print(f'Local variable since function: {var_local}')

        var_global = 'NEW_GLOBAL'   # var_global cannot be wrote without the reserved word global (1)

        def nested_function():
            var_nested = 'NESTED'   # This variable will be destoyed after executing the function
            nonlocal var_local
            print(f'Local variable since nested function: {var_local}')
            var_local = 'NEW_LOCAL' # var_local is wrote and can be updated  (2)

        nested_function()
        print(f'Local variable after executing the nested function: {var_local}')

    _print()
    print(f'Global variable after the execution: {var_global}')


    # Example
    def show_counter():
        print(counter)

    def modify_counter(c):
        global counter
        counter = c

    modify_counter(5)
    show_counter()


def functions():
    print(' 3. Functions '.center(DASH,'-'))

    # Assign functions
    def sum(a, b):
        return a + b
    
    my_function = sum
    print(f'Assign functions: my_function(5,4) => {my_function(5,4)}')

    # Functions as arguments
    def operation(a,b,sum):
        return sum(a, b)    
    
    print(f'Functions as arguments: operation(5,2,sum) => {operation(5,2,sum)}')

    # Return functions
    def return_function():
        return sum
    
    my_function = return_function()
    print(f'Return functions: my_function(5,1) => {my_function(5,1)}')

    # Lambda functions (anonym functions)
    print('\nLambdas')

    # my_function = def sum(a, b): return a + b     # We cannot use this syntax
    my_lambda_function = lambda a, b: a + b

    print(f'Lambda functions: my_lambda_function(2,3) => {my_lambda_function(2,3)}')

    # Lambda functions (without args)
    my_lambda_function = lambda: 'Lambda function without arguments'
    print(f'Lambda functions (without arguments): my_lambda_function() => {my_lambda_function()}')

    # Lambda functions (with default args)
    my_lambda_function = lambda a=4, b=5: a + b 
    print(f'Lambda functions (with default args): my_lambda_function() => {my_lambda_function()}')

    # Lambda functions (with args and kwargs)
    my_lambda_function = lambda *args, **kwargs: len(args) + len(kwargs) 
    print(f'Lambda functions (with args and kwargs): my_lambda_function(1, 2, 3, a=5, b=2) => {my_lambda_function(1, 2, 3, a=5, b=2)}')

    # Closures - are functions that contains other functions
    print('\nClosures')

    def operation(a, b):
        def sum():
            return a + b
        return sum

    my_closure = operation(5, 6)
    print(f'Closure functions: {my_closure()}')
    print(f'Closure functions (without assign): {operation(5, 6)()}')


    # Closures and lambdas
    def operation(a, b):
        return lambda : a + b

    my_closure_lambda = operation(5, 6)
    print(f'Closure lambda functions: {my_closure_lambda()}')
    print(f'Closure lambda functions (without assign): {operation(5, 6)()}')

    # Decorators - Functions that receive one function and return other function to extends functionality
    # 1. Decorator function
    # 2. Function to decorate
    # 3. Decorated function
    print('\nDecorators')
    
    def decorator_function(function_to_decorate):
        def decorated_function():
            print('Before the function_to_decorate()')
            function_to_decorate()
            print('After the function_to_decorate()')

        return decorated_function

    @decorator_function
    def function_to_decorate():
        print('Hello from function_to_decorate()')

    function_to_decorate()

    # Generators - Function to return one by one the results
    # 1. Use yield instead of return
    print('\nGenerators')

    def generator():
        yield 1
        yield 2
        yield 3
    
    gen = generator()

    print(f'Generator functions (1): {next(gen)}')
    print(f'Generator functions (2): {next(gen)}')
    print(f'Generator functions (3): {next(gen)}')
    # print(f'Generator functions (4): {next(gen)}') # Raise StopIteration

    for gen in generator():
        print(f'Generator iteration: {gen}')

    multiply = (value*value for value in range(4))
    print(f'Generator implicit expression: {next(multiply)}')
    print(f'Generator implicit expression: {next(multiply)}')
    print(f'Generator implicit expression: {next(multiply)}')
    print(f'Generator implicit expression: {next(multiply)}')

    list_1 = ['Juan', 'Perez']
    generator_1 = ( value for value in list_1 )
    print(f'Generator expression: {next(generator_1)}')

    # Comprehensions
    print('\nComprehensions')

    evens = [value for value in range(10) if value % 2 == 0]
    print(f'Comprehensions (evens): {evens}')


    # Separating evens an ods
    ods = []
    evens = []

    [ evens.append(x) if x % 2 == 0 else ods.append(x) for x in range(10) ]

    print('Comprehensions (evens and ods):', ods, evens)

    # List of lists
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]

    # Converting nested list in one list
    simple_list = [ value 
        for sublist in nested_list 
        for value in sublist 
    ]
    print('Nested comprehensions: {}'.format(simple_list))

    simple_list_evens = [ value 
        for sublist in nested_list 
        for value in sublist 
        if value % 2 == 0
    ]

    print('Nested comprehensions: {}'.format(simple_list_evens))

    # keywords
    print('\nKeywords')
    print('Keyboards in python:')
    print(keyword.kwlist)

if __name__ == '__main__':
    nested_functions()
    scopes()

    # First class citizens
    functions()
