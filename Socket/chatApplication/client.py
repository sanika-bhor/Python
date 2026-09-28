import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",5000))

while True:
    msg=input("You: ")
    client.send(msg.encode("utf-8"))
    response=client.recv(1024)
    if msg =="exit":
        break
    print("server says: "+response.decode("utf-8"))


client.close()