'''Section 19 Handling Exceptions
    - BaseException
        - Exception
            - ArithmeticError
                - ZeroDivisionError
            - OSError
                - FileNotFoundError
                - PermissionError
            - RuntimeError
            - LookupError
                - IndexError
                - KeyError
            - SyntaxError
                - IndentationError
            - TypeError
            - ValueError
'''

# Creating my own Exception class
class MyException(Exception):
    def __init__(self, message):
        self.message = message

def probing_excepts(a, b):
    result = None
    try:
        result = a / b
        raise MyException('Raising Error')
    except ZeroDivisionError as err:
        print('ERROR:',err)
    except TypeError as err:
        print('ERROR:',err)
    except Exception as err:
        print('ERROR:',err)
    else:
        print('WITHOUT ERRORS, RESULT:',result)
    finally:
        print('EVEN IF THERE ARE ERRORS, WILL PASS HERE')
        
    return result
    

def run():
    probing_excepts(10, 0)
    probing_excepts(2,'AB')
    probing_excepts(1,3)
    
    
    
    print('Bye')
        



if __name__ == '__main__':
    run()