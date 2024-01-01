from connection import Net

class VRPV8(Net):
    def __init__(self):
        super().__init__('huawei_vrpv8', '192.168.88.201', 'huaweiuser', '7ujmNHY^')

    def get_config(self):
        cmd = 'dis cur'
        info = self.device.send_command(cmd)
        config_info = (info.split('aaa')[1])
        return config_info
    
    def get_interfaces(self):
        cmd = 'dis ip int bri'
        info = self.device.send_command(cmd)
        interfaces_info = []
        for line in info.split('VPN')[1:]:
            data = line.split()
            if_name = data[0]
            if_ip = data[1]
            if_status = data[-2]
            interfaces_info.append({'name':if_name, 'ip':if_ip, 'status':if_status})
        return interfaces_info
    
    def reconver_interface(self, if_name):
        cmd_list = [f'int {if_name}', 'undo shut']
        self.device.send_command(command_string=cmd_list, expect_string=r']')

    def get_route(self):
        cmd = 'dis ip routing'
        info = self.device.send_command(cmd)
        route_info = '\n'.join([line for line in info.split('\n') if '/' in line])
        return route_info
    
    def post_route(self, dst_n, mask, next_hop):
        cmd_list = ['sys im', f'ip route-static {dst_n} {mask} {next_hop}']
        for cmd in cmd_list:
            for cmd in cmd_list:
                self.device.send_command(command_string=cmd, expect_string=r']')

    def monitor(self):
        cmd = 'dis cpu'
        info = self.device.send_command(cmd)
        line = info.split('Max CPU Usage')[0].split('five seconds:')[1]
        line_list = line.split('%')
        cpu_5s = line_list[0][-1]
        cpu_1m = line_list[1][-1]
        cpu_5m = line_list[2][-1]
        cpu_info = {'cpu 5s':cpu_5s, 'cpu 1m':cpu_1m, 'cpu 5m':cpu_5m}
        return cpu_info

