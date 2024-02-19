# Écrire un programme qui ne fait rien (exécute une boucle vide) 
# et affiche un message « bip » à chaque SIGINT. 
# À la réception du sixième 
# signal, le programme affiche « bye » et se termine.


import signal, sys

compteur = 0

def traitant(_signum, _ignore):
    """fonction appellée quand on reçoit SIGINT"""
    global compteur  # <- la variable compteur est la variable globale, elle "survit" à la fonction
    # compteur vaut le nombre de fois précédentes où traitant a été appellé
    compteur += 1
    if compteur < 6 :
        print("bip")
    else:
        print("bye")
        sys.exit(0)


# installe le traitant
signal.signal(signal.SIGINT, traitant)

## boucle infinie, attente active
while True: 
    pass
