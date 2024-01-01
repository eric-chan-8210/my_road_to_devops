from connection import Net

class ISO_XE:
    def __init__(self):
        super.__init__('cisco_xe', '192.168.88.200', 'admin', 'cisco')

    def get_config(self):
        cmd = 'show run'
        info = self.dev_conn.send_command(cmd)
        config_info = info.split('platform console serial\n!')[1]
        return config_info
    
    def get_interfaces(self):
        cmd = 'show ip int bri'
        info = self.dev_conn.send_command(cmd)
        interfaces_info = []
        for line in info.split('\n')[1:]:
            data = line.split()
            if_name = data[0]
            if_ip = data[1]
            phy_status = data[-2]
            pro_status = data[-1]
            interfaces_info.append({'name':if_name, 'ip':if_ip, 'status':phy_status, 'protocol':pro_status})
        return interfaces_info
    
    def reconver_interface(self, if_name):
        cmd_list = [f'int {if_name}', 'shutdown', 'no shut']
        self.dev_conn.send_config_set(cmd_list)

    def get_route(self):
        cmd = 'show ip route'
        info = self.dev_conn.send_command(cmd)
        route_info = '\n'.join([line for line in info.split('\n') if '/' in line])
        return route_info
    
    def post_route(self, dst_n, mask, next_hop):
        cmd = [f'ip route {dst_n} {mask} {next_hop}']
        self.dev_conn.send_config_set(cmd)

    def monitor(self):
        cmd = 'show process cpu'
        info = self.dev_conn.send_command(cmd)
        line = info.split('PID Runtime')[0].split('five seconds:')[1]
        line_list = line.split('%')
        cpu1_5s = line_list[0][-1:]
        cpu2_5s = line_list[1][-1:]
        cpu_1m = line_list[2][-1:]
        cpu_5m = line_list[3][-1:]
        cpu_info = {'cpu1 5s':cpu1_5s, 'cpu2 5s':cpu2_5s, 'cpu 1m':cpu_1m, 'cpu 5m':cpu_5m}
        return cpu_info


