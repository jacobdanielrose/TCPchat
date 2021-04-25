#############################
#     TCP Server v0.0.1     #
#############################


import socket
import threading

# Connection Data
host = '192.168.178.66'  # TODO: automate to detect IP-address of computer.
port = 5555


# Sending messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Handling messages from clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except Exception:
            # Removing and closing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request and Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print and broadcast nickname
        print('Nickname is {}'.format(nickname))
        broadcast('{} joined!'.format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == '__main__':
    # Starting Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    # Lists for clients and their nicknames
    clients = []
    nicknames = []

    receive()
