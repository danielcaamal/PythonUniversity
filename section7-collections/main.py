'''Section 8 Collections in Python'''

def lists():
    names = ['Juan', 'Karla', 'Ricardo', 'Maria']
    for name in names:
        print(name)
    
    print('Juan' in names)
    names.append('Roberto')
    names.insert(0, 'Luisa')
    names.remove('Maria')
    names.pop()
    del names[0]
        
    print(names[0::2])
    names.clear()
    print(names)
    del names

def tuples():
    names = ('Juan', 'Karla', 'Ricardo', 'Maria')
    print(names.index('Maria'))
    
    
def homework_8():
    '''Print all natural numbers divisibles by 3 in 0 - 10'''
    print([i for i in range(11) if i % 3 == 0])
    
def homerwork_9():
    '''Given a tuple (13, 1, 8, 3, 2, 5, 8), create a list that only include the numbers bellow 5 using a for loop'''
    numbers = (13, 1, 8, 3, 2, 5, 8)
    print([i for i in numbers if i < 5])
    
def sets():
    big_planets = {'Earth', 'Saturn', 'Jupyter'}
    small_planets = {'Earth', 'Mercury', 'Mars'}
    small_planets.add('Venus')
    
    print(big_planets.difference(small_planets))
    big_planets.remove('Earth')


def dicts():
    dictionary = {
        'IDE': 'Integrated Development Environment',
        'OOP': 'Object Oriented Programming',
        'DBMS': 'Database Management System'
    }
    print(dictionary)
    print(dictionary.keys())
    print(dictionary.values())
    print(dictionary.items())
    print(dictionary.get('RDBMS', False))
    
    

if __name__ == '__main__':
    lists()
    homework_8()
    tuples()
    homerwork_9()
    sets()
    dicts()