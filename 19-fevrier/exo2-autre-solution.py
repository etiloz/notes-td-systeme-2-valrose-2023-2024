# Écrire un programme qui ne fait rien (exécute une boucle vide) 
# mais qui reçoit un signal signal.SIGALRM toutes les secondes, 
# et affiche alors un message « bip ». À la réception du sixième 
# signal, le programme affiche « bye » et se termine.

# fonctions utiles
# signal.signal(signum, handler): installe un traitant de signal
# signal.alarm(delay): installe un minuteur


import signal, sys

# installe un minuteur
signal.alarm(1)

## boucle infinie
compteur = 0
while True: 
    signal.pause() # <- bloquant jusqu'à l'arrivée d'un signal (par exemple SIGALRM)
    compteur += 1
    if compteur < 6 :
        print("bip")
        signal.alarm(1)
    else:
        print("bye")
        sys.exit(0)