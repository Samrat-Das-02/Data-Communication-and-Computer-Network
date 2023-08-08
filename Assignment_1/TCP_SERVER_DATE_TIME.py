#SERVER SIDE
import socket
import datetime

TCP_PORT =20000
IP_ADDR='127.0.0.1'
BUF_SIZE =50
print("Server create a socket ")
# create socket
k=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind socket
k.bind((IP_ADDR, TCP_PORT))
print("Server listening ")
k.listen(1)
con,addr=k.accept()
print("Connection established, connection address is  : ")
print(addr)

#recieved message from the client
data=con.recv(BUF_SIZE)
print("Request from the client : ",data.decode())

#fetching the date and time 
curr_time=datetime.datetime.now().strftime("%d-%m-%y   %H:%M:%S")
response=f"Current date and time : {curr_time}"

#give the data to the client
con.sendall(response.encode())

print("Server send the response to the client and closing the connection")

con.close()
