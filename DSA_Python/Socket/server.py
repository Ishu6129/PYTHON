import socket
import threading

# Server configuration
HOST = '172.16.162.54'  # Localhost (use your IP for real network communication)
PORT = 12345  # Port to listen on

# List of connected clients
clients = []


# Function to handle client messages
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)

    try:
        while True:
            msg = conn.recv(1024).decode('utf-8')  # Receive message
            if msg == 'exit':
                print(f"[DISCONNECT] {addr} disconnected.")
                break

            print(f"[{addr}] {msg}")
            broadcast(f"{addr}: {msg}", conn)  # Broadcast message to all clients
    except ConnectionResetError:
        print(f"[DISCONNECT] {addr} disconnected.")
    finally:
        clients.remove(conn)
        conn.close()


# Broadcast a message to all clients except the sender
def broadcast(msg, sender_conn):
    for client in clients:
        if client != sender_conn:
            client.send(msg.encode('utf-8'))


# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
