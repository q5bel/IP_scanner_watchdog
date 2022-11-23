import threading
import socket
import ipaddress
from pprint import pprint
from server import *


print('---------- Start checking IP in list -----------')

# все основные действия
network = socket.gethostbyname(socket.gethostname()).split('.')
del network[-1]
net = ''
for i in network:
    net += i + '.'

ip_list = ipaddress.ip_network(f'{net}0/24')

for ip in ip_list:
    ptk = threading.Thread(target=check_ip, args=[str(ip)])
    ptk.start()


ptk.join()

pprint(up_ip)
print('----------------- DONE -----------------')
