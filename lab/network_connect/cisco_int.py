from netmiko import ConnectHandler
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')
secret = getpass('Enable: ')
dev_info = {'device_type':'cisco_xe', 'ip':'192.168.88.200', 'username':username, 'password':password, 'secret':secret}

dev_con = ConnectHandler(**dev_info)
dev_con.enable()

cmd = ['int g3', 'ip add 200.1.1.2 255.255.255.252', 'no shut']
show_int = 'show ip int bri'

dev_con.send_config_set(cmd)

result = dev_con.send_command(show_int)
print(result)

dev_con.disconnect()