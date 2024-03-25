import select, socket, sys
HOST = "127.0.0.1"  # or 'localhost' or '' - Standard loopback interface address
PORT = 2003  # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen()
listened_descriptors = [serversocket, 0]
while len(listened_descriptors) > 0:
    (readable, _, _) = select.select(listened_descriptors, [], [])
    for s in readable:
        if s == serversocket:  # serversocket receives a connection
            (clientsocket, (addr, port)) = s.accept()
            print("connection from:", addr, port)
            listened_descriptors.append(clientsocket)
        elif s == 0:
            for sock in listened_descriptors:
                if sock != 0 and sock != serversocket:
                    sock.shutdown(socket.SHUT_WR)
                    sock.close()
            sys.exit(0)
        else:  # data is sent from given client
            data = s.recv(MAXBYTES)
            if len(data) > 0:
                s.sendall(data)
            else:  # client has disconnected
                s.close()
                listened_descriptors.remove(s)
