#import random 
#import time
#import socket
#a = input()
#b = input()
#c = input()

#print("WardenDos by Jjuz0")
#print(f'Цель:' {a} )
#print(f'CPS:' {b} )

#print(f"Атака на" {c} ":" random.randint(23, 100))
#exit()
#import random 
#import time
#import socket

#a = input()
#b = input()
"""
a = "ab.luver.one"
b = 100
print("WardenDos by Jjuz0")
print(f'Цель: {a}')
print(f'CPS: {b}')

print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
print(f"Атака на {a}: {random.randint(23, 100)}")
exit()
"""

import socket
import random 
import time
URL = input("Введите айпи(полный адрес! Пример: google.com): ")
CPS = input("Введите CPS Для атаки: ")
Time = input("Введите Время в секундах: ")



def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as err:
        print(f"Ошибка: {err}")

url = URL
ip = get_ip_address(url)
print(f"WardenDoS V2 by Jjuz0")
print(f"Цель: {url}")
print(f"CPS: {CPS}")
while int(Time) > 0:
    cps2 = random.randint(23, int(CPS))
    time.sleep(random.uniform(0.05, 2))
    print(f"Атака на {ip} : {cps2} CPS")
    Time = int(Time) - 1









































































































































    