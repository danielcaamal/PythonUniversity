DASH = 50

def docstrings():
    '''
    Docstrings:
    This is an documentation of the function:
    :str message This is string to use the principal function of str methods:
    :return None:

    ''' 
    print(' 1. Docstrings '.center(DASH,'-'))

    # Documentation
    print(docstrings.__doc__)


def capitalize():
    print(' 2. Capitalize '.center(DASH,'-'))

    message = 'hello world'
    print(f'Original string: {message}')

    # Capitalize
    print(f'Capitalize string: {message.capitalize()}')


def concatenation():
    print(' 3. Concatenation '.center(DASH,'-'))

    # Automated concatenation
    message1 = 'Hello' + 'World'
    print(f'Concatenation: {message1}')
    message2 = 'Hello' 'World' # Without the plus
    message2 += 'From' 'Python'
    print(f'Concatenation: {message2}')


def split():
    print(' 4. Split '.center(DASH,'-'))
    message = 'hello,world'
    print(f'Original string: {message}')

    # Split
    splitted_arr = message.split(',')
    print(f'Split string: {splitted_arr}')


def join():
    print(' 5. Join '.center(DASH,'-'))
    splitted_arr =  ['Hello', 'World']
    print(f'Original array: {splitted_arr}')

    # Join
    joined_str= ','.join(splitted_arr)
    print(f'Join string: {joined_str}')

    string = 'helloworld'
    joined_str2 = '.'.join(string)
    print(f'Join string: {joined_str2}')

    dictionary = {
        'first_name': 'Juan',
        'last_name': 'Juarez'
    }
    joined_str3 = '-'.join(dictionary.keys())
    print(f'Join string: {joined_str3}')
    joined_str4 = '-'.join(dictionary.values())
    print(f'Join string: {joined_str4}')

def formatting():
    print(' 6. Formatting '.center(DASH,'-'))
    name = 'John'
    last_name = 'Smith'
    age = 28
    salary = 5000
    person = ('Karla', 'Gomez', 3000)
    person_dict = {'name': 'Karla', 'last_name': 'Gomez', 'age': 20, 'salary': 4000}

    print('- Using str simple format')
    message = "My name is %s and I'm %d years old" % (name, age)
    print(f'Message with simple format: {message}')

    message = "Hello %s %s, your salary is %.2f " % person
    print(f'Message with simple format: {message}')

    message = "Hello %s %s, your salary is %.2f "
    print(f'Message with simple format separated: {message%person}')

    print('\n- Using placeholder formats')
    message = "Hello {} {}, your salary is {:.2f}".format(name, last_name, salary)
    print(f'Message with placeholder formats: {message}')

    message = "Hello {0} {2}, your salary is {1:.2f}".format(name, salary, last_name)
    print(f'Message with placeholder formats (with order): {message}')

    message = "Hello {name} {last_name}, your salary is {salary:.2f}".format(**person_dict)
    print(f'Message with placeholder formats (with kwargs): {message}')

    print('\n- Using f-strings or template literals')
    message = f"Hello {name} {last_name}, your salary is {salary:.2f}" # interpolations
    print(f'Message with f-strings: {message}')

    print('\n- Using print formatting')
    print(name, last_name, salary, sep=', ')


def scape_characters():
    print(' 7. Scape characters '.center(DASH,'-'))

    print('- Escaping \\')
    result = 'Hello \' world \\'
    print(result)

    print('\n- Backspace')
    result = 'Deleting the dot.\b'
    print(result)

    print('\n- Raw Strings')
    result = r'This is a: \n raw string'
    print(result)

def unicode_characters():
    print(' 8. UNICODE characters '.center(DASH,'-'))
    print('Simple notation: \u2665')
    print('Extended notation: \U0001F9A0')
    print('Hexadecimal notation: \x41')

def ascii_characters():
    print(' 9. ASCII characters '.center(DASH,'-'))
    character = chr(65)
    print(f'ASCII notation: {character}')

def byte_literals():
    print(' 10. Byte literals '.center(DASH,'-'))
    bytes_characters = b'Hello World'

    print(f'Bytes characters: {bytes_characters}')
    print(f'Byte character: {bytes_characters[0]}')
    print(f'Char character: {chr(bytes_characters[0])}')

    string = 'Hello World from Python (with an ñ)'
    print(f'Original string: {string}')
    
    bytes = string.encode('UTF-8')
    print(f'Bytes encoded: {bytes}')

    string_decoded = bytes.decode('UTF-8')
    print(f'String decoded: {string_decoded}')

    # Handling bytes literal in files
    with open('./section29-advanced-python/GlobalMentoring.txt',encoding='UTF-8') as msg:
        msg = msg.read()
        # print(msg)


def other_str_functions():
    print(' 11. Other str functions '.center(DASH,'-'))

    msg1 = ' Python is Great '
    print(f'Original string: {msg1}')

    # Count function
    with open('./section29-advanced-python/GlobalMentoring.txt',encoding='UTF-8') as msg2:
        msg2 = msg2.read()
        print(f'Count function: {msg2.count("Universidad")}')

    # Upper function
    print(f'Upper function: {msg1.upper()}')

    # Lower function
    print(f'Lower function: {msg1.lower()}')

    # Startswith function + Standardization
    print(f'Startswith function: {msg1.lower().startswith("p")}')

    # Endswith function + Standardization
    print(f'Endswith function: {msg1.lower().endswith("on")}')

    # Is lower function
    print(f'Is lower function: {msg1.islower()}')

    # Is upper function
    print(f'Is upper function: {msg1.isupper()}')

    # Ljust, Rjust and Center function
    print(f'Ljust function {msg1.ljust(30,"*")}')
    print(f'Ljust function {msg1.rjust(30,"*")}')
    print(f'Ljust function {msg1.center(30,"*")}')

    # Replace function
    print(f'Replace function: {msg1.replace(" ","-")}')

    # Strip function
    print(f'Strip function: {msg1.strip()}')


if __name__ == '__main__':
    # Handling strings
    docstrings()
    capitalize()
    concatenation()
    split()
    join()
    formatting()
    scape_characters()
    unicode_characters()
    ascii_characters()
    byte_literals()
    other_str_functions()