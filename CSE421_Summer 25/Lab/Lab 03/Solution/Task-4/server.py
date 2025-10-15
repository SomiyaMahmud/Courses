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
                working_hours = int(msg)
                salary = 0
                if working_hours <= 40:
                    salary = working_hours*200
                else:
                    salary = 8000 + (working_hours-40)*300  
                conn.send(f"The person's salary: {salary}".encode(format))

    conn.close()