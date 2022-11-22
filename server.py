import os
from datetime import datetime
import socket
import threading

start_time = datetime.now()
print('Start checking IP in list', start_time)


def check_ip(ip):
    comm = "ping -c 1 " + ip
    data = os.popen(comm).readlines()
    if 'ttl' in str(data[2]):
        print(ip + ' -----> IP is OK')
    else:
        print(ip + ' -----> IP is not response')


ip_list = []
network = socket.gethostbyname(socket.gethostname())


for last_digit in range(256):
    ip_list.append(f'192.168.1.{last_digit}')

for ip in ip_list:
    ptk = threading.Thread(target=check_ip, args=[ip])
    ptk.start()

ptk.join()

end_time = datetime.now()

print('Done at:', end_time - start_time)

