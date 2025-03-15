import socket
from Display_Config import *

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_COMMANDS = ("/dc", "/disconnect")

# Encode input and its length
def encode(input_str: str):
    input_encoded = input_str.encode(FORMAT)
    send_length = str(len(input_encoded)).encode(FORMAT)
    # Ensure fixed-length header
    send_length += b' ' * (HEADER - len(send_length))
    return send_length, input_encoded


def sendUsername(username: str):
    send_length, user = encode(username)
    client.send(send_length)
    client.send(user)
    print(client.recv(1000).decode(FORMAT))


def send(msg: str):
    send_length, message = encode(msg)
    client.send(send_length)
    client.send(message)
    print(client.recv(1000).decode(FORMAT))


def clientStart():
    connected = True
    while connected:
        msg = input("Input message (/dc or /disconnect to exit): ")
        if msg in DISCONNECT_COMMANDS:
            connected = False

        send(msg)


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    #get username first then start client chat
    username = valid_username("Enter your username: ")
    sendUsername(username)
    clientStart()
