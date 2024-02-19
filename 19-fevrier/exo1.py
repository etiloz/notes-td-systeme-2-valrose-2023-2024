import signal, sys, os, time

## prend en argument de ligne de commande une durée en secondes
## s'endort pendant cette durée
## si jamais reçoit un signal SIGINT pendant qu'il dort, 
## affiche "J'ai reçu SIGINT" et termine

# fonctions utiles
# signal.signal(signum, handler) : Met en place le traitant handler pour le signal signum
# time.sleep(secs) : Suspend l'exécution du programme pendant secs secondes


def handler(sig, ignore):
    print("J'ai reçu SIGINT")
#    sys.exit(0)  # <- on peut aussi terminer le programme ici (c'est le comportement par convention d'un SIGINT)

print("Mon PID est", os.getpid(), f"utile pour m'envoyer SIGINT depuis un autre terminal avec kill -2 {os.getpid()}")
signal.signal(signal.SIGINT, handler) # Met en place le nouveau traitant 
time.sleep(int(sys.argv[1])) # Suspend l'exécution du programme pendant la durée spécifiée
print("Fin du programme") # Cette ligne ne sera jamais exécutée
sys.exit(0)
