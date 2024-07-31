import socket
import json
from os import system, name

localIP     = "0.0.0.0"
localPort   = 4568
bufferSize  = 512

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

arr = []

print("UDP server up and listening")
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    byte_message = bytesAddressPair[0]
    message = byte_message.decode('utf-8')
    arr.append(message)
    clear()
    for txt in arr:
        print(txt)
