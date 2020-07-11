import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

byte_len = 20

full_msg = ''
new_msg = True
while True:
    msg = s.recv(byte_len)
    if new_msg:
        msg_len = int(msg[:HEADERSIZE])
        new_msg = False
        print(f"new message length is  {msg_len}")
    
    #continuously to add new info
    full_msg += msg.decode("utf-8")

    #check if the full mesg_len has been received
    if len(full_msg)-HEADERSIZE == msg_len:
        print(f"full msg recvd:{full_msg[HEADERSIZE:]}")
        #reset the flag and clear the messsage.
        new_msg = True
        full_msg = ""

