import time
import random



def reg(database, username, password, level):
    user_id = str(random.randint(10000,20000))
    database[user_id] = {'username':username, 'password':password, 'level':level}
    print(f'User {username} is recorded, User ID is {user_id}')
    return database, user_id, username

def find_name(database, user_id, username):
    if username in database[user_id]['username']:
        print(f'User {username} in database')

def find_id(database, user_id):
    if user_id in database:
        print(f'User {database[user_id]['username']}: {user_id}') 

def login(database, username, password):
    for user_id in database:
        if database[user_id]['username'] == username:
            if database[user_id]['password'] == password:
                print(f'User {username} login success, level is {database[user_id]['level']}')



