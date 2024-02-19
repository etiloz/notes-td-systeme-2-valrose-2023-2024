# Écrire un programme qui ne fait rien (exécute une boucle vide) 
# mais qui reçoit un signal signal.SIGALRM toutes les secondes, 
# et affiche alors un message « bip ». À la réception du sixième 
# signal, le programme affiche « bye » et se termine.

# fonctions utiles
# signal.signal(signum, handler): installe un traitant de signal
# signal.alarm(delay): installe un minuteur


import signal, sys

compteur = 0

def traitant(_signum, _ignore):
    """fonction appellée quand on reçoit SIGALRM"""
    global compteur  # <- la variable compteur est la variable globale, elle "survit" à la fonction
    # compteur vaut le nombre de fois précédentes où traitant a été appellé
    compteur += 1
    if compteur < 6 :
        print("bip")
        # on programme l'envoi du prochain signal dans 1 sec
        signal.alarm(1)

    else:
        print("bye")
        sys.exit(0)


# installe le traitant
signal.signal(signal.SIGALRM, traitant)

# installe un minuteur
signal.alarm(1) # revient à faire os.kill(signal.SIGALRM, os.getpid()) mais dans 1 sec

## boucle infinie, attente active
while True: 
    pass
    #  juste pour remplir, on aurait pu faire aussi
#    x = 0
    # ou encore   
#    signal.pause()