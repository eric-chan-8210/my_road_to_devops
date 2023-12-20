from netmiko import ConnectHandler

device_info = {'device_type':'huawei', 'ip': '192.168.88.201', 'username': 'huaweiuser', 'password':'6yhnMJU&'}

show_run = 'dis cur'

dev_connect = ConnectHandler(**device_info)

result = dev_connect.send_command(show_run)

tmp = 'aaa' + result.split('aaa')[1]

with open('huawei_config.txt','w') as file1:
    file1.write(tmp)
    file1.close()
    dev_connect.disconnect()
with open('huawei_config.txt') as file2:
    data = file2.read()
    file2.close()

