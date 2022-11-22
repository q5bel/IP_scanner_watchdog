import socket

network = socket.gethostbyname(socket.gethostname())
network_split = network.split('.')
x = ''
for num in network_split[:-1]:
    x += num + '.'


print(x)

print(network)