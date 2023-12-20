from netmiko import ConnectHandler
from getpass import getpass
from datetime import date

now = date.today()
username = input('Username: ')
password = getpass('Password: ')
secret = getpass('Enable: ')

dev_info = {'device_type':'cisco_xe', 'ip':'192.168.88.200', 'username':username, 'password':password, 'secret':secret}

dev_con = ConnectHandler(**dev_info)
dev_con.enable()

cmd = 'show run'

result = dev_con.send_command(cmd)
with open ('cisco_config_'+str(now)+'.txt','w') as file:
    file.write(result)
file.close()
dev_con.disconnect()
