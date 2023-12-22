from netmiko import ConnectHandler
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')
secret = getpass('Enable: ')
dev_info = {'device_type':'cisco_xe', 'ip':'192.168.88.200', 'username':username, 'password':password, 'secret':secret}

dev_con = ConnectHandler(**dev_info)
dev_con.enable()

show_cpu = 'show proc cpu'

result = dev_con.send_command(show_cpu)

line = result.split('CPU utilization for')[1].split('PID Runtime')[0].strip()

data = [one[-1] for one in line.split('%') if one != '']
print(data)