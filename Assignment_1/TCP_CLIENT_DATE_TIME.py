#CLIENT SIDE
import socket
import datetime

TCP_PORT =20000
IP_ADDR='127.0.0.1'
BUF_SIZE =50
print("Client create a socket")
k=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#establish a connection with the server 
k.connect((IP_ADDR, TCP_PORT))

#request date and time from the server
MSG="Give me the date and time"
k.send(MSG.encode())

print("Take the response from the server")
#taking reply from the server
data=k.recv(BUF_SIZE)
print(data.decode())

