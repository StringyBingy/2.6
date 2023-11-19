import socket

MAX_PACKET = 1024
IP = '127.0.0.1'
PORT = 6969


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = ' '
    try:
        my_socket.connect((IP, PORT))
        while response != '':
            my_socket.send(input('enter command: ').encode())
            response = my_socket.recv(MAX_PACKET).decode()
            print(response)
    except socket.error as err:
        print('socket error with error code' + err)
    finally:
        print('disconnecting...')
        my_socket.close()
        print('disconnected successfully')


if __name__ == '__main__':
    main()
