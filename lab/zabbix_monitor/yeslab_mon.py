
from utils import INFLUX
from pyzabbix.api import ZabbixAPI

class ZABBIX:
    def __init__(self):
        self.host_list = ['ACC1','ACC2','CO1','CO2']
        self.need_list = ['Interface Gi1(): Bits sent', 'Interface Gi1(): Bits received','ICMP response time']
        self.zapi = ZabbixAPI(url='http://183.6.42.206:3031', user='Admin', password='zabbix')
        self.host_id_list = [info['hostid'] for info in self.zapi.host.get(monitord_host=1, output='extend') if info['host'] in self.host_list]
        self.influx = INFLUX()

    def get_item_dict(self, hostid, need_list):
        result = self.zapi.item.get(hostids=hostid)
        return {info['itemid']:info['name'] for info in result if info['name'] in need_list}


    def zabbix_monitor(self):
        for i in range(len(self.host_id_list)):
            host_id = self.host_id_list[i]
            device_name = self.host_list[i]
            item_dict = self.get_item_dict(host_id, self.need_list)
            print(item_dict)
            for i in range(len(item_dict)):
                mon_data = self.zapi.item.get(itemids=list(item_dict.keys()))
                item_name = mon_data[i]['name']
                item_value = mon_data[i]['lastvalue']
                self.influx.write('Local' + device_name, [item_name, float(item_value)])
    
    def close(self):
        self.zapi.user.logout()
