import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",5000))

msg="I Want Protection Plan for my policy"

client.send(msg.encode("utf-8"))
response=client.recv(1024)

print("server says: "+response.decode("utf-8"))
client.close()