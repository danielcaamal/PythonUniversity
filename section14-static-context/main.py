from constants import MY_CONSTANT
from Person import Person

'''Section 14 - Static context (Classes) in Python''' 
class MyClass():
    # A Python Class variable is shared by all instances of a Class
    class_var = 'Class var'
    
    def __init__(self, instance_var):
        # A Python Instance variable are owned by an instance of a Class
        self.instance_var = instance_var
    
    # A Python static method don't receive self, and only can be called using the class itself
    @staticmethod
    def static_method():
        return MyClass.class_var
    
    # A Python Class methods allows to access to variables and functions by the parameter 'cls'
    @classmethod
    def class_method(cls):
        return cls.class_var
    
    # Instance methods can access to static variables and methods, class methods and instance variables
    def instance_method(self):
        self.class_method()
        self.static_method()
        self.class_var
        self.instance_var
        print('instance_method()')
    

def run():
    # Instance variable
    my_class1 = MyClass('instance_var1')
    print('Instance variable:', my_class1.instance_var)
    
    my_class2 = MyClass('instance_var2')
    print('Instance variable:', my_class2.instance_var)
    
    # Class variables
    print('Class variable:',my_class1.class_var)
    print('Class variable:',my_class2.class_var)
    
    # Creating a class variable
    MyClass.class_var2 = 'Class var2' 
    print('Class variable created:',my_class2.class_var2)
    
    # Calling static methods
    print('Static method:', MyClass.static_method())
    
    # Calling class methods
    print('Class method:', MyClass.class_method())
    
    # Calling instance methods
    my_class1.instance_method()
    
    # Using constants
    print('Constant:', MY_CONSTANT)
    
    # Applications (Counter Objects)
    person1 = Person('Juan', 32)
    print(person1)
    person2 = Person('Sandra', 20)
    print(person2)
    
    Person.generate_next_id()
    
    person3 = Person('Maria', 35)
    print(person3)
    

if __name__ == "__main__":
    run()