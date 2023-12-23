import json

with open('client.json') as f:
    j2p = json.load(f)
print(j2p.keys())

new_client = {}
new_client['id'] = j2p['id']
new_client['mac'] = j2p['mac']
new_client['ip'] = j2p['ip']
new_client['ip6'] = j2p['ip6']
new_client['description'] = j2p['description']
new_client['firstSeen'] = j2p['firstSeen']
new_client['lastSeen'] = j2p['lastSeen']
new_client['manufacturer'] = j2p['manufacturer']
new_client['os'] = j2p['os']
new_client['user'] = j2p['user']
new_client['vlan'] = j2p['vlan']
new_client['ssid'] = j2p['ssid']
new_client['switchport'] = j2p['switchport']
new_client['wirelessCapabilities'] = j2p['wirelessCapabilities']
new_client['smInstalled'] = j2p['smInstalled']
new_client['recentDeviceMac'] = j2p['recentDeviceMac']
new_client['clientVpnConnections'] = j2p['clientVpnConnections']
new_client['lldp'] = j2p['lldp']
new_client['cdp'] = j2p['cdp']
new_client['status'] = j2p['status']
with open('new_client.py','a') as f:
    f.write(str(new_client))
f.close()