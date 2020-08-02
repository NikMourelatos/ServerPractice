import socket
import time
import os


class ClientCodes:
    HANDSHAKE = 1
    PICTURE = 2

############################################################
def sendImage(sock):
    picturePath = input(str("Input the Path to picture:"))
    f = open(picturePath,'rb')
    l = f.read(1024)
    while l:
        sock.sendall(l)
        print("Sent ",repr(l))
        l = f.read(1024)
    print("Image has been sent")




############################################################
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 4444)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    msg = sock.recv(1028)

    if msg == bytes(ClientCodes.HANDSHAKE):
        print("Initializing Handshake")
        time.sleep(0.2)
        sock.sendall(bytes(ClientCodes.HANDSHAKE))
        time.sleep(0.2)
        sock.sendall(bytes(ClientCodes.PICTURE))
        time.sleep(0.2)
        sendImage(sock)



finally:
    print('closing socket')
    sock.close()
