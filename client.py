#############################
#     TCP Client v0.0.1     #
#############################

import socket
import threading


# Listening to server and sending nickname
def receive():
    while True:
        try:
            # receive message from server
            # If 'NICK', send nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # close connection if error
            print('An error occurred!')
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


if __name__ == '__main__':
    # Choosing Nickname
    nickname = input('Choose your nickname: ')

    # Connecting to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.178.66', 5555))  # TODO: automate to detect IP-address of computer.

    # starting threads for listening and writing
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
