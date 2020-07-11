import socket
import time

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

print("Waiting for connections")
# we only accep one for now
clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")

#build a message
while True:

    #add header to i
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    clientsocket.send(bytes(msg,"utf-8")) 

    time.sleep(3)

clientsocket.close()