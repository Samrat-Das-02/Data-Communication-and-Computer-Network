#Client side 
import socket 

TCP_PORT = 20000
IP_ADDR='127.0.0.1'
BUF_SIZE=100
k=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
k.connect((IP_ADDR,TCP_PORT))

expression=input("Enter the mathematical expression : ")
k.send(expression.encode())

result=k.recv(BUF_SIZE)
print("Client recieved the result from the server : ")
print(result.decode())

k.close()