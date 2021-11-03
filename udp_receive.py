#!/usr/bin/python3
import _thread, time, socket

# Empty data variable where incoming messages will be stored
data = ''   # Declare an empty variable

# Prepare UDP port for listening ################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 7601
sock.bind(('', port))  # We are using port "port'" to bind to


while True:

    print ('THE PACKET RECEIVED BY THE MAIN BODY IS: ' + data, end='\r')

    #  Receive the data ################################
    data_raw, addr  = sock.recvfrom(1024)
    data            = data_raw.decode()    # My test message is encoded
    
    #  Print the data   ################################
    if data:
        print ('THE PACKET RECEIVED BY THE MAIN BODY IS: ' + data, end='\r')
        print()
        data = ''   # Empty the variable ready for the next one
