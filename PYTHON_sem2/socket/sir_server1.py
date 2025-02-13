import socket
def receive_file(file_path, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
        s.listen(1)
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        print(f"Connected to {addr}")
        # Open the file in binary mode for writing
        with open(file_path, 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break  # Break if no more data to receive
                # Write the received data to the file
                file.write(data)
        print("File received successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection and the socket
        conn.close()
        s.close()
file_path = 'D:\\received_file.txt'
host = '127.0.0.1'  
port = 9999 
receive_file(file_path, host, port)
