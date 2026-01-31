import socket
format = 'utf-8'
HEADER = 64


server = socket.gethostbyname(socket.gethostname())
port = 4949
disconnect_msg = "End"

addr = (server, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    message = msg.encode(format)
    msg_length = len(msg)
    send_length = str(msg_length).encode(format)
    send_length += b" "*(HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(format))   #ack print

msg = f'The hostname of client is {socket.gethostname()} and the IP is {server}'

while True:
    prompt = input("Enter working hours: ")
    if prompt == disconnect_msg:
        send(disconnect_msg)
        break
    else:
        send(prompt)
