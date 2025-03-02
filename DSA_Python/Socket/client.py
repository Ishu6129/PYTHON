import socket
import threading

# Client configuration
HOST = '172.16.162.54'  # Localhost (use your IP for real network communication)
PORT = 12345 # Server port


# Receive messages from the server
def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')  # Receive message from server
            print(msg)
        except:
            print("Disconnected from server")
            break


# Send messages to the server
def send_messages(sock):
    while True:
        msg = input()
        if msg == 'exit':
            sock.send(msg.encode('utf-8'))
            break
        sock.send(msg.encode('utf-8'))


# Start the client
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to the chat server. Type 'exit' to leave.")

    # Start receiving and sending threads
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

    # Wait for the send thread to finish before closing
    send_thread.join()
    client.close()


if __name__ == "__main__":
    start_client()