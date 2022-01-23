from Connection import PoolCursor
from User import User
from Logger_base import log

class UserDao():
    _TABLE = 'users'
    _SELECT = f'SELECT * FROM {_TABLE} ORDER BY id DESC;'
    _INSERT = f'INSERT INTO {_TABLE}(username, password) VALUES(%s, %s);'
    _UPDATE = f'UPDATE {_TABLE} SET username=%s, password=%s WHERE id=%s;'
    _DELETE = f'DELETE FROM {_TABLE} WHERE id=%s;'

    @classmethod
    def select(cls):
        users = []
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECT)
            res = cursor.fetchall()
            for user in res:
                users.append(User(**user))
        return users

    @classmethod
    def insert(cls, user: User):
        with PoolCursor() as cursor:
            print(user)
            values = (user.username, user.password,)
            cursor.execute(cls._INSERT,values)
            log.debug(f'INSERTED: {user}')
            return cursor.rowcount
    
    @classmethod
    def update(cls, user: User):
        with PoolCursor() as cursor:
            values = (user.username, user.password, user.id,)
            cursor.execute(cls._UPDATE,values)
            log.debug(f'UPDATED: {user}')
            return cursor.rowcount

    @classmethod
    def delete(cls, user: User):
        with PoolCursor() as cursor:
            values = (user.id,)
            cursor.execute(cls._DELETE,values)
            log.debug(f'DELETED: {user}')
            return cursor.rowcount