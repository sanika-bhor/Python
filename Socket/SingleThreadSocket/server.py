import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("0.0.0.0",5000))
server.listen()
print("server is listening for client...")

connection, address = server.accept()
print("client connected: ",address)

def clientconnection():

    while True:
        data=connection.recv(1024)
        print("client says:  "+data.decode("utf-8"))
        msg=input("you: ")
        if msg =="exit":
            break
        connection.send(msg.encode("utf-8"))

    connection.close()

t1=threading.Thread(target=clientconnection)
t1.start()
t1.join()
server.close()