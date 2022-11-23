import os
import threading
import socket
import ipaddress
"""
Здесь мы проверяем все ip адреса в диапазоне в локальной подсети
нужно сделать:
проверка - майнер ли это, задать словарь логинов паролей, вывод и мониторинг хэшрейта
+ отдельный файл, где бесконечный цикл с проверкой
вопросы::::
как сделать так, чтобы записывались активные майнеры и при этом опрашивались данные адреса постоянно
нужен ли постоянный опрос для ВСЕЙ сети?

"""
print('---------- Start checking IP in list -----------')


def check_ip(ip):
    comm = "ping -c 1 " + ip
    data = os.popen(comm).readlines()
    for line in data:
        if 'ttl' in line:
            print(ip + ' -----> IP is up')


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

print('----------------- DONE -----------------')