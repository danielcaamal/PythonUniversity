'''
    Object to connect to the Database using the model Person
    DAO (Data Access Object)
    CRUD (Create Read Update Delete)
'''

from logger_base import log
from Connection import PoolCursor
from Person import Person
import json
from faker import Faker
import pandas as pd

fake = Faker()

class PersonDAO():
    _TABLE = 'person'
    _SELECT = f'SELECT * FROM {_TABLE} ORDER BY id DESC;'
    _INSERT = f'INSERT INTO {_TABLE}(first_name, last_name, email) VALUES(%s, %s, %s);'
    _UPDATE = f'UPDATE {_TABLE} SET first_name=%s, last_name=%s, email=%s WHERE id=%s;'
    _DELETE = f'DELETE FROM {_TABLE} WHERE id=%s;'

    @classmethod
    def select(cls):
        people = []
        with PoolCursor(cursor=PoolCursor.REAL_DICT_CURSOR) as cursor:
            cursor.execute(cls._SELECT)
            res = cursor.fetchall()
            for person in res:
                people.append(Person(**person))
            df = pd.DataFrame(res)
            print(df)
        return df

    @classmethod
    def insert(cls, person):
        cls._validate_person(person)
        with PoolCursor() as cursor:
            values = (person.first_name, person.last_name, person.email,)
            cursor.execute(cls._INSERT,values)
            log.debug(f'INSERTED: {person}')
            return cursor.rowcount
    
    @classmethod
    def update(cls, person):
        cls._validate_person(person)
        with PoolCursor() as cursor:
            values = (person.first_name, person.last_name, person.email, person.id,)
            cursor.execute(cls._UPDATE,values)
            log.debug(f'UPDATED: {person}')
            return cursor.rowcount

    @classmethod
    def delete(cls, person):
        cls._validate_person(person)
        with PoolCursor() as cursor:
            values = (person.id,)
            cursor.execute(cls._DELETE,values)
            log.debug(f'DELETED: {person}')
            return cursor.rowcount

    @classmethod
    def _validate_person(cls, person):
        if isinstance(person, Person):
            return True
        raise Exception('You only can add Person Objects')
                


if __name__ == '__main__':
    # Insert statement
    rowcount = PersonDAO.insert(Person(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email()    
    ))
    log.info(f'ROWS AFFECTED (INSERT): {rowcount}')

    # Select statement
    people = PersonDAO.select()
    for person in people:
        log.debug(person)
    
    # Update statement
    rowcount = PersonDAO.update(Person(
        id=11,
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email()    
    ))
    log.info(f'ROWS AFFECTED (UPDATE): {rowcount}')

    # Delete statement 
    rowcount = PersonDAO.delete(Person(
        id=people[0].id, 
    ))
    log.info(f'ROWS AFFECTED (DELETE): {rowcount}')