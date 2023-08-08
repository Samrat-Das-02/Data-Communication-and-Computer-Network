#server side 
import socket 

TCP_PORT = 20000
IP_ADDR='127.0.0.1'
BUF_SIZE=100
k=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Server is listening on ")
k.bind((IP_ADDR,TCP_PORT))
k.listen(1)
client_socket,addr=k.accept()
print("Connection is established, connectionn address")
print(addr)

data=client_socket.recv(BUF_SIZE)
expression=data.decode()
print("The expression recieved from the client is : ",expression)

try:
    result=eval(expression)
    forwarding_result=f"The result of the mathematical expression is : {result}"
    client_socket.sendall(forwarding_result.encode())
except Exception as e:
    print("There is an error in the expression recieved from the client : ",e)
    er=f"Error - Invalid input : {e}"
    client_socket.sendall(er.encode())
print("Server send the response to the client and closing the connection")

client_socket.close()



