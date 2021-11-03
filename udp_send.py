#!/usr/bin/python3
import socket
import sys 

# Read arguments from the command line
# should be used like this:
#		 python3 udp_send.py [message] [port]
# 	i.e. python3 udp_send.py something 7500
list_of_arguments = sys.argv

message = str(list_of_arguments[1])


ip = '127.0.0.1'
# port = 7500
port = int(list_of_arguments[2])

sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(message,"utf-8"),(ip,port))