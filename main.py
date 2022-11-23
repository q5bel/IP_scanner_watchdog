import threading
from pprint import pprint
from ip_scan import *


print('---------- Start checking IP in list -----------')
# все основные действия
ip_list = get_ip_list()

for ip in ip_list:
    ptk = threading.Thread(target=check_ip, args=[str(ip)])
    ptk.start()
ptk.join()

pprint(up_ip)
print('----------------- DONE -----------------')
