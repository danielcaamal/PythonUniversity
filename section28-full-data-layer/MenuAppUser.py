'''Responsabilities:
    - 1) List users
    - 2) Add user
    - 3) Update users
    - 4) Delete users
    - 5) Exit
'''

from UserDao import UserDao, User
from Connection import PoolCursor

DASH = 100
menu = '''\n
{}
1) List Users
2) Add User
3) Update User
4) Delete User
5) Exit
                        *This is an example of using a data layer connected to one postgres database

Select an option (1-5): '''.format('USERS'.center(DASH,'-'))

def run():
    option = None
    while option != 5:
        option = input(menu)

        # SELECT
        if option == '1':
            print(' User List '.center(DASH,'-'))
            users = UserDao.select()
            for user in users:
                print(user)
            print('Total Results: {}'.format(len(users)))
        
        # INSERT
        elif option == '2':
            username = input('Enter username: ')
            password = input('Enter password: ')
            if username == '' or password == '':
                print('Username and password cannot be blank.')
            user = User(username=username,password=password)
            inserts = UserDao.insert(user)
            print('Total Inserts: {}'.format(inserts))

        # UPDATE
        elif option == '3':
            id = input('Select the user (id) to update: ')
            username = input('Enter the new username: ')
            password = input('Enter the new password: ')
            if username == '' or password == '' or id == '':
                print('Username, id and password cannot be blank.')
            user = User(username=username,password=password,id=id)
            updates = UserDao.update(user)
            print('Total Updates: {}'.format(updates))

        # DELETE
        elif option == '4':
            id = input('Select the user (id) to delete: ')
            if  id == '':
                print('Id cannot be blank.')
            user = User(username=username,password=password,id=id)
            deletes = UserDao.delete(user)
            print('Total Deletes: {}'.format(deletes))

        else:
            print('Wrong option, select an option (1-5).')
    print(' Bye :) '.center(DASH,'-'))


def basic_configuration():
    with PoolCursor() as cursor:
        try:
            query = '''CREATE TABLE users(
                id serial PRIMARY KEY NOT NULL,
                username VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            );'''
            cursor.execute(query)
        except:
            pass

if __name__ == '__main__':
    basic_configuration()
    run()