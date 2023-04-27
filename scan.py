import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input(str("Target IP: "))

#Banner
print("_" * 50)
print("Scanning Started at: " + str(datetime.now()))
print("_" * 50)

try :

    #Scan Ports

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Retrun Open Port
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open ".format(port))
        s.close()

#Exceptions 
except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()
except socket.error:
        print("\ Host not responding :()")
        sys.exit()

