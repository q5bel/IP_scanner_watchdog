import os
import threading

print('---------- Start checking IP in list -----------')


def check_ip(ip):
    comm = "ping -c 1 " + ip
    data = os.popen(comm).readlines()
    for line in data:
        if 'ttl' in line:
            print(ip + ' -----> IP is up')


ip_list = []
for last_digit in range(256):
    ip_list.append(f'192.168.1.{last_digit}')

for ip in ip_list:
    ptk = threading.Thread(target=check_ip, args=[ip])
    ptk.start()

ptk.join()

print('----------------- DONE -----------------')