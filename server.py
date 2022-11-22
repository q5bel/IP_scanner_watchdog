import os
import threading
import socket
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


ip_list = []
network = socket.gethostbyname(socket.gethostname())
network_split = network.split('.')
ip_head = ''
for num in network_split[:-1]:
    ip_head += num + '.'
for last_digit in range(256):
    ip_list.append(f'{ip_head}{last_digit}')

for ip in ip_list:
    ptk = threading.Thread(target=check_ip, args=[ip])
    ptk.start()

ptk.join()

print('----------------- DONE -----------------')