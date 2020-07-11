import socket
import pyperclip as clip

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

#after connection
#just listen to the port
byte_len = 1028
HEADERSIZE = 10

full_msg = ''
new_msg = True
while True:
    msg = s.recv(byte_len)
    if new_msg:
        try:
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
            print(f"new message length is  {msg_len}")
        except:
            continue
    
    #continuously to add new info
    full_msg += msg.decode("utf-8")

    #check if the full mesg_len has been received
    if len(full_msg)-HEADERSIZE == msg_len:
        print(f"msg put on clip board:{full_msg[HEADERSIZE:]}")
        #do something with the received message
        #here just paste it on the clip board
        #clip.copy(full_msg) cannot do this. it becomes a self circulating loop on the same machine. 
        clip.copy(full_msg[HEADERSIZE:])

        #reset the flag and clear the messsage.
        new_msg = True
        full_msg = ""
        