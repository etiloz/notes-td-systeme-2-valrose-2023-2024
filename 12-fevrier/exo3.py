# Écrivez un programme Python qui, par le biais de créations de 
# processus et de recouvrements, exécute la suite de commandes 
# who ; pwd ; ls -l 
# (rappel : le point-virgule signifie qu’une commande est exécutée 
# lorsque la commande précédente est terminée).

import os

pid_fils = os.fork()
if pid_fils == 0:
    os.execvp("who", ["who"])
os.wait()
pid_fils = os.fork()
if pid_fils == 0:
    os.execvp("pwd", ["pwd"])
os.wait()
pid_fils = os.fork()
if pid_fils == 0:
    os.execvp("ls", ["ls", "-l"])
os.wait()