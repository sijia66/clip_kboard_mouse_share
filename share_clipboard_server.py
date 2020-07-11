import socket
from pyperclip import waitForNewPaste
import time

HEADERSIZE = 10 #for socket communication

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print('listening for connections...')

clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")

#for now just try one time
#wait for new paste, it will take time
while True:
    msg = waitForNewPaste()
    print(f'got a new message {msg}')

    #once it gets it, it will send to the client
    #add header to i
    msg = f"{len(msg):<{HEADERSIZE}}"+msg
    print(msg)
    clientsocket.send(bytes(msg,"utf-8")) 
    #time.sleep(0.01)
    

#close the socket
clientsocket.close()