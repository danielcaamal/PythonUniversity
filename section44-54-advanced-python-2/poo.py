from dataclasses import dataclass
import inspect
from typing import ClassVar


DASH = 50

def title(text):
    return print(f' {text} '.center(DASH,'-'))

def subtitle(text):
    print()
    return print(f' {text} '.center(DASH,' '))

def block(text):
    return print(f'\n - {text}')

def attributes():
    title('0. Attributes Types')

    class MyClass():
        def __init__(self, public, protected, private):
            self.public = public            # This can be writted
            self._protected = protected     # This shouldn't be writted
            self.__private = private        # This cannot be writted

# Override constructors
def override_constructors():
    title('1. Override')
    class Person():
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        @classmethod
        def create_empty_person(cls):
            return cls(None, None)

        @classmethod
        def create_person(cls, **args):
            return cls(**args)


        # Representation Objects
        # Using __rpr__ instead __str__, __rpr__ is used by programmers
        def __repr__(self):
            return f'{self.__class__.__name__}(first_name:{self.first_name}, last_name:{self.last_name})'

        # Focused to the final user
        def __str__(self):
            return f'{self.__class__.__name__}: {self.first_name} {self.last_name}'

        # Format give more details, __format__ is called by default in prints
        def __format__(self, __format_spec: str):
            return f'{self.__class__.__name__} with name {self.first_name} and lastname {self.last_name}'

    person1 = Person('Juan', 'Perez')
    # using __str__
    print(f'Original constructor: {person1!s}')

    # using __repr__
    empty_person = Person.create_empty_person()
    print(f'Constructor Override (empty values): {empty_person!r}')

    # using __format__
    person2 = Person.create_person(first_name='Daniel', last_name='Flores')
    print(f'Constructor Override: {person2}\n')


def inheritance():
    title('2. Inheritance')
    class Parent():
        def __init__(self):
            print('Initiliazing parent...')
        
        def method(self):
            print('Parent method...')

    class Child1(Parent):
        pass

    parent1 = Parent()
    parent1.method()

    subtitle('Order Inheriting')
    
    block('Inheriting init')

    child1 = Child1() # Child calls to the init parent

    block('Overriding init')

    class Child2(Parent):
        def __init__(self):
            print('Initiliazing child...')

    child2 = Child2() # Child calls to the init parent

    block('Inheriting init and using init')
    class Child3(Parent):
        def __init__(self):
            super().__init__()
            print('Initiliazing child...')

    child3 = Child3() # Child calls to the init parent


    subtitle('Simple inheritance')
    class SimpleList():
        def __init__(self, elements):
            self._elements = list(elements)

        def add(self, element):
            self._elements.append(element)
        
        def __getitem__(self, index):
            return self._elements[index]

        def order(self):
            self._elements.sort()

        def __len__(self):
            return len(self._elements)
        
        def __repr__(self):
            return f'{self.__class__.__name__}({self._elements!r})'

    simple_list = SimpleList([5, 12, 8, 2, 9, 10])
    print(f'Simple list: {simple_list}')

    class OrderedList(SimpleList):
        def __init__(self, elements=[]):
            super().__init__(elements)
            self.order()
        
        def add(self, element):
            super().add(element)
            self.order()
    
    ordered_list = OrderedList([5, 3, 8, 12, 9, 10])
    
    print(f'Ordered list: {ordered_list}')

    print(f'Size Ordered list: {len(ordered_list)}')

    class IntList(SimpleList):
        def __init__(self, elements=[]):
            for element in elements:
                self._validate(element)
            super().__init__(elements)
        
        def add(self, element):
            self._validate(element)
            super().add(element)

        def _validate(self, element):
            if not isinstance(element, int):
                raise ValueError('This element is not int.')

    try:
        int_list = IntList(['err', 1, 2, 4, 5]) # Throw an error
    except ValueError as e:
        print('Error:', e)

    int_list = IntList([ 1, 2, 4, 5])
    print(f'Int list: {int_list}')
    
    subtitle('Multiple Inheritance')

    class OrderedIntList(IntList, OrderedList):
        pass

    ordered_int_list = OrderedIntList([5, 6, 7, 1, 2])

    print(f'Ordered int list: {ordered_int_list}')

    try:
        ordered_int_list2 = OrderedIntList(['a', 6, 7, 1, 2])   # Throw an error
    except ValueError as e:
        print(f'Error: {e}')


    subtitle('Class Decorators (meta-programming)')

    def decorator_repr(cls):
        print(f'1. Executing the decorator on: {cls.__name__}')

        attributes = vars(cls)
        for key, value in attributes.items():
            print(key, value)
        
        init_sign = inspect.signature(cls.__init__)
        print(f'Init sign: {init_sign}')

        init_params = list(init_sign.parameters)[1:]
        print(f'Init params: {init_params}')

        # Check if the param has property
        properties = [ param 
            for param in init_params 
            if isinstance(attributes.get(param), property)
        ]
        print(f'Init properties: {properties}')

        def repr_method(self):
            print('3. Repr result')

            # Getting class name
            name_class = self.__class__.__name__

            # Getting parameters (Generator expression)
            generator_attr = (f'{name}={getattr(self,name)!r}' for name in properties)
            args_list = ', '.join(list(generator_attr))
            print(f'List args: {args_list}')
            
            # Returning the dynamic __repr__ 
            return f'{name_class}({args_list})'
        
        setattr(cls, '__repr__', repr_method)
        return cls

    @decorator_repr
    class Person():
        def __init__(self, first_name, last_name, age):
            print('2. Initializing Person...')
            self._first_name = first_name
            self._last_name = last_name
            self._age = age     # Is not a property
        
        @property
        def first_name(self):
            return self._first_name
        
        @property
        def last_name(self):
            return self._last_name

    person1 = Person('Juan', 'Perez', 12)
    print(person1)
    print('4. Source:\n', inspect.getsource(person1.__repr__))


def data_classes():
    title('3. Inheritance')

    @dataclass(eq=True, frozen=True)
    class Address():
        street : str
        number : int = 0

    # Eq makes every instance different
    # frozen makes the instances inmutables
    @dataclass(eq=True, frozen=True)
    class Person():
        first_name: str
        last_name:  str
        counter: ClassVar[int] = 0
        address: Address

        # Validations
        def __post_init__(self):
            if not self.last_name or not self.first_name:
                raise ValueError('The name cannot be empty')

    
    address1 = Address('27', '543')
    person1 = Person('Juan', 'Perez', address1)
    print(f'{person1}!r')

    print(f'Class Variables: {Person.counter}')
    print(f'Instance Variables: {person1.__dict__}')

    try:
        empty_person = Person('Daniel', '', '')
    except ValueError as e:
        print('ERROR:', e)

    address2 = Address('54', '321')
    person2 = Person('Maria', 'Perez', address2)

    print(f'The objects are equal? {person2 == person1}')

    collection = {person1, person2} # only accepts inmutable objects
    print(collection)





if __name__ == '__main__':
    override_constructors()
    inheritance()
    data_classes()