import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            msg = client_socket.recv(1024).decode("utf-8")
            print(msg)
    except ConnectionResetError:
        print("\n\nDisconnected from server")

def main():
    ip = "192.168.223.137"
    port = 2670
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    name = input("Enter your name: ")
    client.send(name.encode("utf-8"))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    try:
        while True:
            msg = input(f'[ {name} ]: ')
            client.send(msg.encode("utf-8"))
    except KeyboardInterrupt:
        print("\nExiting...")
        client.send("close".encode("utf-8"))
        client.close()
main()
