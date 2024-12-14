import socket
client=socket.socket()
client.connect(('localhost',9999))  #its a host and port address 
name=input("Enter your name")
client.send(bytes(name,'utf-8'))  #conver bytes and send to server
    
print(client.recv(1024))