import time
from local import ZABBIX

def run():
    local_ins = ZABBIX()
    local_ins.zabbix_monitor()

if __name__ == "__main__":
    while True:
        run()
        time.sleep(30)