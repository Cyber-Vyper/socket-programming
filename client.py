import socket 

PORT = 8000
HEADER = 64
FORMAT = 'utf-8'
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

DISCONNECT_MESSAGE = "Disconnected!"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
     message = msg.encode(FORMAT)
     msg_length = len(message)
     send_length = str(msg_length).encode(FORMAT)
     send_length += b' ' * (HEADER - len(send_length))
     client.send(send_length)
     client.send(message)
     print(client.recv(1048).decode(FORMAT))
while True:     
     send(input("Enter message: "))
     

     