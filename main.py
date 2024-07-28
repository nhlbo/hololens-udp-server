import socket
import json
from os import system, name

localIP     = "0.0.0.0"
localPort   = 4567
bufferSize  = 512

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print("UDP server up and listening")
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    byte_message = bytesAddressPair[0]
    message = json.loads(byte_message.decode('utf-8'))
    distances = message["distances"]
    clear()
    print(f'''
    distances between 2 left fingers: {distances[0] * 100:.2f} cm
    distances between 2 right fingers: {distances[1] * 100:.2f} cm

    distances between 2 palms: {distances[2] * 100:.2f} cm

    distances between left palm and ground: {distances[3] * 100:.2f} cm
    distances between right palm and ground: {distances[6] * 100:.2f} cm

    distances between left palm and wall (parallel vector): {distances[4] * 100:.2f} cm
    distances between right palm and wall (parallel vector): {distances[7] * 100:.2f} cm

    distances between left palm and wall (eye gaze): {distances[5] * 100:.2f} cm
    distances between right palm and wall (eye gaze): {distances[8] * 100:.2f} cm
    ''')
