import socket

def send_file(file_path, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                # Send the data over the socket
                s.sendall(data)

        print("File sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the socket
        s.close()

file_path = 'D:\\example.txt'
host = '127.0.0.1'  
port = 9999  

send_file(file_path, host, port)
