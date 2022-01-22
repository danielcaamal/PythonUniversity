from logger_base import log

class Person():

    def __init__(self, id=None, first_name=None, last_name=None, email=None):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return str({
            'id': self._id,
            'first_name':self._first_name,
            'last_name':self._last_name,
            'email': self._email,
        })

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

if __name__ == '__main__':
    # Probing the class
    person1 = Person(id=1, first_name='Daniel', last_name='Caamal', email='danielcaamal@email.com')
    log.debug(person1)

    # Simulating an insert to the database
    person2 = Person(first_name='Juan', last_name='Perez', email='jperez@email.com')
    log.debug(person2)
