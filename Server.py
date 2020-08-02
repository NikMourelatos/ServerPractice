import socket
import TensorTry


class ClientCodes:
    HANDSHAKE = 1
    PICTURE = 2


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 4444))

    sock.listen(1)
    print('starting up on {} port {}'.format('localhost', 4444))
    while True:
        print("Started waiting for client")
        connection, client_address = sock.accept()
        try:
            print("Client Connected ", client_address)
            connection.send(bytes(ClientCodes.HANDSHAKE))

            while True:
                if connection.recv(1028) == bytes(ClientCodes.HANDSHAKE):
                    msg = connection.recv(1025)
                    switcher(msg, connection)
                    break;


        finally:
            sock.close()


def switcher(arg, connection):
    switch = {
        bytes(ClientCodes.PICTURE): getPicture
    }
    func = switch.get(arg)
    func(connection)


def getPicture(connection):
    file = "recieved_file.jpeg"
    with open(file, 'wb') as f:
        print("file opening")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            else:
                f.write(data)
    TensorTry.UseAlgo(file)


if __name__ == '__main__':
    main()
