import socket
from datetime import datetime
import random

MAX_PACKET = 4
QUEUE_LEN = 1
SERVER_NAME = 'coolest server'
PORT = 6969
IP = '127.0.0.1'


def return_current_time():
    """
    this function returns the current time
    :return: current time
    :return type: str
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def return_rand_number():
    """
    this function uses rand library to create random number
    :return: random number between 1 and 10 inclusive
    :return type: int
    """
    number = random.randint(1, 10)
    return str(number)


def check_request(request):
    """
    this funtion checks the request/message from the client and acts accordingly
    :param request: message from client
    :param type: str
    :return: according to the request the appropriate response
    :return type: str
    """
    if request == 'TIME':
        print('sending current time...')
        return return_current_time()

    elif request == 'NAME':
        print('sending server name...')
        return 'the servers name is: ' + SERVER_NAME

    elif request == 'RAND':
        print('sending random number...')
        return 'random number generated: ' + return_rand_number()

    elif request == 'EXIT':
        return ''

    elif request == '':
        return 'request must be 4 bytes'

    else:
        return 'no command found such as ' + request


def connect_to_client(server_socket):
    """

    :param server_socket:
    :return:
    """
    server_socket.bind((IP, PORT))
    server_socket.listen(QUEUE_LEN)
    client_socket, client_address = server_socket.accept()
    return client_socket, client_address


def close_server_socket(server_socket):
    """

    :param server_socket:
    :return:
    """
    print('closing...')
    server_socket.close()
    print('closed server successfully!')


def disconnect_client(client_socket):
    """

    :param client_socket:
    :return:
    """
    print('disconnecting client...')
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket, client_address = connect_to_client(server_socket)
        response = ' '
        try:
            while True:
                request = client_socket.recv(MAX_PACKET).decode()
                print('server received ' + request)
                response = check_request(request)
                client_socket.send(response.encode())
        except socket.error as err:
            print('received socket error on client socket with error code ' + str(err))
        finally:
            disconnect_client(client_socket)
    except socket.error as err:
        print('received socket error on server socket with error code ' + str(err))
    finally:
        close_server_socket(server_socket)


if __name__ == '__main__':
    assert check_request(''), "Request should not be empty"
    main()
