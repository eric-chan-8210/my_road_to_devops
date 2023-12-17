import random
from getpass import getpass
import time


class login:
    def __init__(self, system_name):
        print(system_name)
        self.database = {}
        self.level = 3
        self.sign_up()

    def _get_account(self):
        self.username = input('Input Your Name: ')
        self.password = getpass('Input Your Password: ')

    def sign_up(self):
        self._get_account()
        user_id = str(random.randint(10000,20000))
        self.database[user_id] = {'username':self.username, 'password':self.password, 'level':self.level}
        print(f'User {self.username} is record, User ID is {user_id}')

    def find_id(self, query_id):
        if query_id in self.database:
            print(f'User ID: {query_id} is exist, Username is {self.username}')

    def login(self):
        self._get_account()
        for user_id in self.database:
            if self.database[user_id]['username'] == self.username:
                if self.database[user_id]['password'] == self.password:
                    print(f'User {self.username} login successful, User Level is {self.level}')


system1 = login('Cisco Portal')
system1.login()
time.sleep(2)

system2 = login('Palo Alto Portal')
system2.login()
