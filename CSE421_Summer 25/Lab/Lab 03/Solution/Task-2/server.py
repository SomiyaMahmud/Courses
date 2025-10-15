import socket

server_ip = socket.gethostbyname(socket.gethostname())
port = 4949
disconnect_msg = 'End'
HEADER = 64
format = 'utf-8'

addr = (server_ip, port)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(addr)
print('Server is Starting.....')

# Listening Stage
SERVER.listen()
print("Server is Listening On", server_ip)

# Accepting Stage
while True:
    conn, ADDR = SERVER.accept()
    print("Connected to", ADDR)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(format)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(format)
            if msg == disconnect_msg:
                connected = False
                conn.send(f"Terminating the connection with {ADDR}".encode(format))
            else:
                vowels = "AEIOUaeiou"
                count = 0
                for i in msg:
                    if i in vowels:
                        count +=1
                if count == 0:
                    conn.send("Not enough vowels".encode(format))
                elif count <= 2:
                    conn.send("Enough vowels I guess".encode(format))
                else:
                    conn.send("Too many vowels".encode(format))

    conn.close()