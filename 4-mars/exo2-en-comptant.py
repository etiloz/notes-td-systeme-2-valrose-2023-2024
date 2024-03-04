# Ping-pong de signaux

# 1. Écrire un programme Python qui crée 1 fils, 
# puis attend la fin du fils. Le fils envoie le signal 
# SIGUSR1 au père. À la réception du signal, le père affiche 
# un message puis envoie le signal SIGUSR1 au fils. 
# À la réception du signal, le fils affiche un message 
# puis se termine. Le père attend la fin du fils, 
# affiche un message puis se termine.

# 2. Modifier le programme pour qu'il reçoive un entier n sur 
# la ligne de commande, et modifier le fils et le père 
# pour que l'échange de signaux se passe successivement n fois.

import os, sys, signal, time

n = int(sys.argv[1])

def handler_pere():
    global pid_fils
    print("père: signal reçu")
    os.kill(pid_fils, signal.SIGUSR1)

nb_signaux_recus = 0

def handler_fils():
    global nb_signaux_recus
    print("fils: signal reçu")
    nb_signaux_recus += 1
    if nb_signaux_recus < n:
        os.kill(os.getppid(), signal.SIGUSR1)

def handler_mutualise(_sig, _ignore):
    global pid_fils
    if pid_fils == 0:
        handler_fils()
    else:
        handler_pere()

signal.signal(signal.SIGUSR1, handler_mutualise)
pid_fils = os.fork()
if pid_fils == 0:
    #fils
    pid_pere = os.getppid()
    signal_recu = False  # <- avant le kill, sinon on risque d'écraser le sig_recu=True du handler
    os.kill(pid_pere, signal.SIGUSR1)
    # boucle attente active
    while nb_signaux_recus < n:
        pass
    sys.exit(0)
# père
os.wait()
sys.exit(0)
