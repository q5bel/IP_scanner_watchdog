import os

up_ip = {}


def get_host_name(ip):  # ищем имя хоста по ip-адресу
    comm = f"host {ip}"
    data = os.popen(comm).readlines()
    data = str(data)
    data = data[data.find('pointer') + 8:-5]
    return data


def check_ip(ip): # ищем активные ip-адреса
    comm = "ping -c 1 " + ip
    data = os.popen(comm).readlines()
    for line in data:
        if 'ttl' in line:
            x = get_host_name(ip)
            up_ip[ip] = x
    return up_ip

