from sign import *
from getpass import getpass

database = {}
username = input('Input Your Name: ')
password = getpass('Input Your Password: ')

database, user_id, username = reg(database, username, password, '3')
time.sleep(2)

find_name(database, user_id, username)
time.sleep(2)

find_id(database, user_id)
time.sleep(2)

login(database, username, password)
time.sleep(2)
