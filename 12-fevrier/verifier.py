#!/usr/bin/env python3

# Écrire un programme verifier.py dont l’usage sera 
# ./verifier.py com arg1 .. argn
# et qui lance la commande com arg1 .. argn, 
# signale une éventuelle erreur lors du lancement, attend la fin de 
# l’exécution et précise par un message le résultat (succès ou échec).

# EXEMPLES

# `./verifier.py toto je sais pas`
# affiche
# toto: commande non trouvée
# échec

# `./verifier.py echo hello`
# affiche
# hello
# succès

# `./verifier.py ls je_sais_pas`
# affiche
# ls: je_sais_pas: No such file or directory
# échec

import os, sys

def fils():
    try:
        os.execvp(sys.argv[1], sys.argv[1:])
        #sys.exit(0) # <- ne sera pas exécuté, la commande lancee decidera du code de sortie
    except:
        print(f"commande non trouvée {sys.argv[1]}")
        sys.exit(1)

def pere(pid_fils):
    _pid_fils, status = os.waitpid(pid_fils, 0)
    # marche aussi avec `_pid_fils, status = os.wait()`
    if os.WIFEXITED(status) and os.WEXITSTATUS(status) == 0 :
        print("succès")
    else:
        print("échec")

pid_fils = os.fork()
if pid_fils == 0:
    fils()
else:
    pere(pid_fils)