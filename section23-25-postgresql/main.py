'''Section 23 - 35 PostgreSQL'''

from random import randint
import psycopg2
from faker import Faker

fake = Faker()

def basic_connection(params):
    print('Basic Connection'.center(50,'-'))
    # Database connection
    conn = psycopg2.connect(**params)

    # Cursor connection
    cursor = conn.cursor()
    
    # SELECT statement
    query = 'SELECT * FROM person'
    cursor.execute(query)

    # Getting data
    res = cursor.fetchall()
    for person in res:
        print(person)
    
    # Database disconnection
    cursor.close()
    conn.close()

def context_manager_connection(params):
    print('Context Manager Connection'.center(50,'-'))
    # Database connection
    conn = psycopg2.connect(**params)
    try:
        with conn:
            # WITH conn allows to do the commit automatically
            with conn.cursor() as cursor:
                # INSERT statement
                query = '''
                    INSERT INTO person(first_name, last_name, email) 
                    VALUES (%s, %s, %s)
                '''
                values = (
                    fake.first_name(), 
                    fake.last_name(), 
                    fake.email()
                )
                cursor.execute(query,values)
                inserted_rows = cursor.rowcount
                print(f'INSERTED ROWS: {inserted_rows}')
    except Exception as e:
        print(e)
    finally:
        # If the WITH conn doesn't exist then the we have to do manually the commit
        # conn.commit()
        conn.close()

def using_query_args(params):
    print('Using Query Args'.center(50,'-'))
    # Database connection
    conn = psycopg2.connect(**params)
    try:
        with conn.cursor() as cursor:
            query = '''
                SELECT * FROM person WHERE id in %s
            '''
            values = ((1, 9, 13),)
            cursor.execute(query,values)
            res = cursor.fetchall()
            for person in res:
                print(person)
    except Exception as e:
        print(e)
    finally:
        conn.commit()
        conn.close()


def insert_many_registers(params):
    print('Insert Many Registers'.center(50,'-'))
    # Database connection
    conn = psycopg2.connect(**params)
    try:
        with conn:
            with conn.cursor() as cursor:
                # INSERT MANY
                query = '''
                    INSERT INTO person(first_name, last_name, email) 
                    VALUES (%s, %s, %s)
                '''
                values = []
                for i in range(3):
                    values.append((
                        fake.first_name(), 
                        fake.last_name(), 
                        fake.email()
                    ),)

                cursor.executemany(query,tuple(values))
                inserted_rows = cursor.rowcount
                print(f'INSERTED ROWS: {inserted_rows}')
    except Exception as e:
        print(e)
    finally:
        conn.close()


def update_many_registers(params):
    print('Update Many Registers'.center(50,'-'))
    # Database connection
    conn = psycopg2.connect(**params)
    try:
        with conn:
            with conn.cursor() as cursor:
                # UPDATE ONE
                query = '''
                    UPDATE person 
                    SET email=%s 
                    WHERE id=%s
                '''
                values = (
                    fake.email(),
                    randint(2, 10)
                )

                cursor.execute(query,values)
                updated_rows = cursor.rowcount
                print(f'UPDATED ROWS: {updated_rows}')

                # UPDATE MANY
                query = '''
                    UPDATE person 
                    SET email=%s 
                    WHERE id=%s
                '''
                values = []

                for i in range(2):
                    values.append((
                        fake.email(),
                        randint(2, 10)
                    ),)

                cursor.executemany(query,tuple(values))
                updated_rows = cursor.rowcount
                print(f'UPDATED ROWS: {updated_rows}')
    except Exception as e:
        print(e)
    finally:
        conn.close()

def delete_registers(params):
    print('Delete Many Registers'.center(50,'-'))
    # Database connection
    conn = psycopg2.connect(**params)
    try:
        with conn:
            with conn.cursor() as cursor:
                # Getting the last id
                query = '''
                    SELECT id 
                    FROM person
                    ORDER BY id DESC
                '''
                cursor.execute(query)
                id = cursor.fetchone()

                # DELETE THE LAST REGISTER
                query = '''
                    DELETE FROM person 
                    WHERE id=%s
                '''
                values = (
                    id,
                )
                cursor.execute(query, values)
                deleted_rows = cursor.rowcount
                print(f'DELETED ROWS: {deleted_rows}')


    except Exception as e:
        print(e)
    finally:
        conn.close()

def transacctions(params):
    print('Transacctions'.center(50,'-'))
    # How to handle transactions
    conn = psycopg2.connect(**params)
    try:
        with conn:
            with conn.cursor() as cursor:
                query = '''
                    INSERT INTO person(first_name, last_name, email) 
                    VALUES (%s, %s, %s)
                '''
                values = (
                    fake.first_name(), 
                    fake.last_name(), 
                    fake.email()
                )
                cursor.execute(query, values)               
    except Exception as e:
        print(e)
    finally:
        conn.close()

def run():
    # Connection parameters
    params = {
        'user':'daniel',
        'password':'daniel',
        'host':'192.168.100.32',
        'database':'test',
        'port':'5432'
    }

    
    # Basic connection con PostgreSQL
    basic_connection(params)

    # Context Manager connection
    context_manager_connection(params)

    # Using query args
    using_query_args(params)

    # Insert many registers
    insert_many_registers(params)

    # Update many registers
    update_many_registers(params)

    # Deleting registers
    delete_registers(params)

    # Transactions
    transacctions(params)





if __name__ == '__main__':
    run()