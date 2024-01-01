import datetime
from cisco import ISO_XE
from huawei import VRPV8

def create_email_body(device_name, alert_type, alert_description):
    now = str(datetime.datetime.now()).split('.')[0]
    with open('/template/head.html',encoding='uft-8') as f:
        text_head = f.read()
    with open('/template/body.html',encoding='uft-8') as f:
        text_body = f.read()
    body = text_head + '\n' + text_body.format(device_name, alert_type, alert_description, now)

def cisco_runner():
    device_name = 'CiscoISOXE'
    iso_xe = ISO_XE

    cisco_data = {}
    cisco_data['Config'] = iso_xe.get_config()
    cisco_data['Interfaces'] = iso_xe.get_interfaces()
    cisco_data['routeTable'] = iso_xe.get_route()
    cisco_data['monitor'] = {'cpu':iso_xe.monitor()}

    for interface in cisco_data['interfaces']:
        if interface['status'] != 'up':
            alert_des = f'{device_name} {interface['name']} is down'
            body = create_email_body(device_name, 'Error', alert_des)
            iso_xe.send_mail(subject='Interface Error', body=body)

    dst = '172.16.10.0'
    mask = '255.255.255.0'
    next = '10.1.1.100'
    if dst not in iso_xe['routeTable']:
        iso_xe.post_route(dst, mask, next)
        cisco_data['routeTable'] = iso_xe.get_route()
        print(f'new route to {dst} has been created')

    iso_xe.to_json(cisco_data, 'data/cisco.json')

    iso_xe.dev_conn.disconnect()

def huawei_runner():
    device_name = 'Huawei_VRPv8'
    vrpv8 = VRPV8

    huawei_data = {}
    huawei_data['Config'] = vrpv8.get_config()
    huawei_data['Interfaces'] = vrpv8.get_interfaces()
    huawei_data['routeTable'] = vrpv8.get_route()
    huawei_data['monitor'] = {'cpu':vrpv8.monitor()}

    for interface in huawei_data['Interfaces']:
        if interface['status'] != 'up':
            alert_des = f'{device_name} {interface['name']} is down'
            body = create_email_body(device_name, 'Error', alert_des)
            vrpv8.send_mail(subject='Inetface Error', body=body)

    dst = '172.16.10.0'
    mask = '255.255.255.0'
    next = '10.1.1.100'
    if dst not in huawei_data['routeTable']:
        vrpv8.post_route(dst, mask, next)
        huawei_data['routeTable'] = vrpv8.get_route()
        print(f'new route to {dst} has been created')

    vrpv8.to_json(huawei_data, 'data/huawei.json')

    vrpv8.dev_conn.disconnect()
