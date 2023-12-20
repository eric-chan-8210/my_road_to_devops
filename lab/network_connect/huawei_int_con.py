from netmiko import ConnectHandler

dev_info = {'device_type':'huawei_vrpv8', 'ip':'192.168.88.201', 'username':'huaweiuser', 'password':'6yhnMJU&'}

dev_connect = ConnectHandler(**dev_info)

con_int = ['sys im', 'int g1/0/1', 'undo shut', 'undo portswitch', 'ip add 200.1.1.1 30']

show_int = 'dis ip int brief'

for cmd in con_int:
    dev_connect.send_command(command_string=cmd, expect_string=r']')

result = dev_connect.send_command(show_int)

print(result)
dev_connect.disconnect()