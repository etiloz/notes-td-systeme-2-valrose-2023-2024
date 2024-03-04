# Comptage de signaux

# 1. Écrire un programme Python qui crée 1 fils, puis attend la fin du fils. 
# Le fils envoie le signal SIGUSR1 au père puis se termine.

# 2. Modifier le père pour qu'il affiche un message lorsque le signal SIGUSR1 est capté.

# 3. Modifier le programme pour qu'il reçoive un entier n sur la ligne de commande, et modifier le fils de telle 
# sorte qu'il envoie à la suite n signaux SIGUSR1 au père avant de se terminer.

# 4. Modifier le père pour qu'il compte le nombre de signaux SIGUSR1 reçus ; supprimer tout affichage 
# dans le handler de signal du père, et afficher le nombre final de signaux reçus après la fin du fils.


#### FONCTIONS UTILES
# os.fork() -> renvoie le pid du fils créé au père, 0 au fils
# os.wait() -> renvoie le pid et code de sortie d'un fils qui a terminé (bloquant)
# os.waitpid(pid, 0) -> version où on spécifie le fils qu'on attend
# os.getpid() -> renvoie le pid de soi-même
# os.getppid() -> renvoie le pid du père
# signal.signal(sig, handler) : installe la fonction handler pour réagir à l'arrivée du signal sig
# forme d'un traitant de signal : `def handler(sig, _ignore)` 
# (sig permet de savoir quel signal a déclenché le handler, utile si même handler attaché à plusieurs signaux)
# os.kill(pid, sig) : envoie le signal sig au processus pid
# signal.SIGUSR1 : la constante pour le signal SIGUSR1

import os, signal, sys, time

count = 0

def mon_handler(_sig, _ignore):
    global count
    count += 1
#    print("signal SIGUSR1 reçu")

signal.signal(signal.SIGUSR1, mon_handler)
pid_fils = os.fork()
if pid_fils == 0 :
    pid_pere = os.getppid()
    n = int(sys.argv[1])
    for _ in range(n):
        os.kill(pid_pere, signal.SIGUSR1)
        time.sleep(0.00002) # <- pour espacer les signaux, pour laisser le temps au pere de traiter le signal
    sys.exit(0)
os.wait()
print(f"{count=}, bye")
#sys.exit(0) # <- implicite