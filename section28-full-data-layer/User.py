

class User():
    def __init__(self, id=None, username=None, password=None):
        self._id = id
        self._username = username
        self._password = password

    def __str__(self):
        return str({
            'id': self._id,
            'username': self._username
        })
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password