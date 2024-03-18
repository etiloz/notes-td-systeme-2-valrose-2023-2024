import os, sys
# programme générique client-serveur
# Les deux modules suivants doivent être écrits
# ils sont supposés fournir les deux méthodes
# client.client()
# server.server()

# QUESTION 2.2.1 : changer le programme principal pour communiquer via des tubes nommés
# au lieu de tubes anonymes

# commandes utiles : 
# - `os.mkfifo(nom)`` : crée un tube nommé
# - `os.open(nom, os.O_RDONLY)` : ouvre un tube nommé en lecture
# - `os.open(nom, os.O_WRONLY)` : ouvre un tube nommé en écriture

import os
import client, server

if __name__ == "__main__":

    # version originale (tube anonyme)
    # rfd1, wfd1 = os.pipe()  # tube père vers fils
    # rfd2, wfd2 = os.pipe()  # tube fils vers père

    # version avec tubes nommés
    try: # au cas où les tubes existent déjà 
        os.mkfifo("/tmp/tube1")
    except: pass
    try:
        os.mkfifo("/tmp/tube2")
    except: pass

    # ne pas faire ça, car ça bloque le programme
    # rfd1 = os.open("/tmp/tube1", os.O_RDONLY) # -> bloquant!
    # wfd1 = os.open("/tmp/tube1", os.O_WRONLY)
    # rfd2 = os.open("/tmp/tube2", os.O_RDONLY)
    # wfd2 = os.open("/tmp/tube2", os.O_WRONLY)

    childpid = os.fork()
    if childpid == 0:  # child
        rfd1 = os.open("/tmp/tube1", os.O_RDONLY)
        wfd2 = os.open("/tmp/tube2", os.O_WRONLY)
        server.server(rfd1, wfd2)  # fils éxecute serveur
    else:  # father
        wfd1 = os.open("/tmp/tube1", os.O_WRONLY) # dans le même ordre que le fils
        rfd2 = os.open("/tmp/tube2", os.O_RDONLY)
        client.client(rfd2, wfd1)  # père exécute client
        os.waitpid(childpid, 0)  # attendre fin fils
    sys.exit(0)
