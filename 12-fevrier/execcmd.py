#!/usr/bin/env python3

# Écrire un programme execcmd.py qui exécute une commande Unix qu’on lui 
# passe en paramètre. 
# Exemple d’exécution :
#      ./execcmd.py /bin/ls -Ft /
# Pour écrire ce programme, il faut savoir qu’une variable prédéfinie de 
# type dictionnaire appelée os.environ contient, par convention, 
# les variables d’environnement dans la mémoire d’un processus 

import os, sys
#print(f"{sys.argv=}")
#os.execve(sys.argv[1], sys.argv[1:], os.environ)
# ou encore
#os.execv(sys.argv[1], sys.argv[1:])

# si on veut utiliser le PATH pour trouver le fichier
os.execvpe(sys.argv[1], sys.argv[1:], os.environ)

