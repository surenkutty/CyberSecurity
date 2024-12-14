import socket

servers=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INT is internet protocal socket  #SCOK_STREM to strem the value
print("socket Created")

servers.bind(('localhost',9999))  #to bind connection on host and port
servers.listen(3)  #to listen the connection
print('waiting for connections')

while True:
    client,addr=servers.accept()   #to accept the client
    name=client.recv(1024).decode()  #to decode and get the input
    print("connected With:",addr,name)
    client.send(bytes('Welcome to surendhar','utf-8'))
    client.close()