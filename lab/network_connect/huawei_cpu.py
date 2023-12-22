from netmiko import ConnectHandler

dev_info = {'device_type':'huawei_vrpv8', 'ip':'192.168.88.201', 'username':'huaweiuser', 'password':'7ujmNHY^'}

dev_connect = ConnectHandler(**dev_info)

show_cpu = 'dis cpu'

result = dev_connect.send_command(show_cpu)

cpu_info = result.split('CPU utilization for')[1].split('.')[0]

data = [one[-1] for one in cpu_info.split('%') if one !='']

#data = []                         这个是传统写法
#for one in cpu_info.split('%'):
#    if one !='':
#        data.append(one[-1])

print(data)
dev_connect.disconnect()