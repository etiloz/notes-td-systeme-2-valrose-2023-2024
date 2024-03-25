# 1. Expliquez ce que fait le programme suivant et comment on pourrait le tester 
# à partir de la ligne de commande du shell Unix 
# REPONSE: telnet 127.0.0.1 2123

# 2. Comment faire en sorte qu’une fois un client déconnecté, le serveur ne se 
# termine pas et puisse attendre d’autres clients ?

# 3. Quels défauts cette approche comporte-t-elle ?
# REPONSE:
# - Le serveur ne peut traiter qu'une seule connexion à la fois.
# - on ne peut pas arrêter le serveur proprement, il faut le tuer.

import socket
HOST = "127.0.0.1"  # or 'localhost' or '' - Standard loopback interface address
PORT = 2123  # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
# create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
    # AF_INET: IPv4
    # SOCK_STREAM: TCP
    serversocket.bind((HOST, PORT))  # bind this socket to specific port on host
    serversocket.listen()  # make the socket a listening one
    while True: # question 2
        (sessionsocket, (addr,port)) = serversocket.accept()  
                # blocking; returns if a client connects.
        with sessionsocket:
            print(f"Connected by application: {port} on machine: {addr}")
            data = sessionsocket.recv(MAXBYTES)
            data = data.capitalize()
            while len(data) > 0:  # otherwise means a disconnection from the client side.
                sessionsocket.sendall(data)
                data = sessionsocket.recv(MAXBYTES)