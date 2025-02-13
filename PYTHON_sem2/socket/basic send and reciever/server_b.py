import socket
import threading
ip="192.168.223.137"
port=2670
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
def main():
    server.listen()
    print("server started......")
    while True:
        clientobj,addr=server.accept()
        msg=clientobj.recv(1024).decode("utf-8")
        name=msg
        c=threading.Thread(target=clients,args=(name,clientobj,addr))
        c.start()
        
def clients(n,clnt,adr):
    print("connected to","Name :",n,"having --",adr[0])
    while True:
        mg=clnt.recv(1024).decode("utf-8")
        if mg.lower() == "close":
                print("bye")
                clnt.close()
                break
        elif mg!="":
            print(f"[ {n} ] : {mg}")
    print("client to server cosed for",n)

main()


