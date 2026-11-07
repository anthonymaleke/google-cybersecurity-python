import re
log_data = 'Failed login from 192.168.1.5'
ips = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_data)
print(ips)
