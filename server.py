import socket
import threading

# Set up
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_COMMANDS = ("/dc", "/disconnect")


def handle_client(conn, addr):
    #print(f"[NEW CONNECTION] {addr} connected.")

    # Receive username length first
    username_length = conn.recv(HEADER).decode(FORMAT)
    if username_length:
        username_length = int(username_length.strip())  # Ensure it's an int
        username = conn.recv(username_length).decode(FORMAT)  # Get username
        print(f"\n[NEW CONNECTION] {username} connected.")
        conn.send("Username received".encode(FORMAT))  # Acknowledge username

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length.strip())  # Convert to integer
            msg = conn.recv(msg_length).decode(FORMAT)  # Receive message

            if msg in DISCONNECT_COMMANDS:
                connected = False
                print(f"[DISCONNECTED] {username} has left the chat.")
            else:
                print(f"{username}: {msg}")  # Print message with username
                conn.send("Msg received".encode(FORMAT))  # Send acknowledgment

    conn.close()


def StartServer():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #print(f"[ACTIVATING CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    print("[STARTING] server is starting...")
    StartServer()
