import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of Aarguments")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)

		result = s.connect_ex((target,port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\n Exiting the program!!")
	sys.exit()
except socket.gaierror:
	print("\n Hostname could not be resolved!!")
	sys.exit()
except socket.error:
	print("Server not responding1!")
	sys.exit()
