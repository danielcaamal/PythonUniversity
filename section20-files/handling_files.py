

class HandlingFiles():
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('OPENING THE FILE'.center(50,'-'))
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name
    
    def __exit__(self, type_exception, value_exception, traceback):
        print('CLOSING THE FILE'.center(50,'-'))
        if self.name:
            self.name.close()
