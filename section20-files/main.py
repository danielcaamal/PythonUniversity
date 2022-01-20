''' Section 20 files
    - Handling files
        - "r" - Read    - Deafult value. Opens a file for reading, error if te file does not exist.
        - "a" - Append  - Opens a file por apprending, creates the file if it does not exist.
        - "w" - Write   - Opens a file for writing, creates the file if it does not exist.
        - "x" - Create  - Creates the specified file, returns an error if the file exist.
    - Chosing the type of file handled:
        - "t" - Text - Default value.
        = "b" - Binary - Binary mode (e.g. images).
    - Writing files
    - Reading files
    - Working wth files
'''

'''Section 21 WITH
    - Context Manager (__ENTER__,__EXIT__)
'''

from handling_files import HandlingFiles

def writing_files():
    print('Writing files...')
    try:
        file = open('file.txt','w',encoding='utf8')
        file.write('We are writing in the file\n')
        file.write('Goodbye\n')
    except Exception as e:
        print(e)
    finally:
        file.close()
        
def reading_files():
    print('Reading files...')
    try:
        file = open('file.txt','r',encoding='utf8')
        string = file.read()
        print(string)
    except Exception as e:
        print(e)
    finally:
        file.close()
        
def working_with_files():
    print('Working with files...')
    try:
        # Files iteration
        file = open('file.txt','r',encoding='utf8')
        for line in file:
            print(line)
        file.close()
        
        
        # Read lines
        file = open('file.txt','r',encoding='utf8')
        print(file.readlines())
        file.close()
        
        # Adding infomation
        file = open('file.txt','r',encoding='utf8')
        file2 = open('copy.txt','a',encoding='utf8')
        file2.write(file.read())
        file.close()
        file2.close()
        
    except Exception as e:
        pass
    
def working_with_with():
    print('Working with WITH...')
    with open('file.txt','r',encoding='utf8') as file:
        print(file.read())
        
def handling_files():
    with HandlingFiles('file2.txt') as file:
        print(file.read())


if __name__ == '__main__':
    
    # Working with files
    writing_files()
    reading_files()
    working_with_files()
    
    # Working with files and 'with'
    working_with_with()
    
    # Handling files
    handling_files()
    
    print('FINISH')
    