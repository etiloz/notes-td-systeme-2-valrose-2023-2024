# 1. Modifier ce programme pour qu’il affiche les numéro des 
# processus dans l’ordre dans lequel ils ont été créés.
# solution "triche": on attend que le fils precedent ait termine
# avant de creer le suivant
import errno, os, sys
nbChildren = 20
for i in range(nbChildren):
    pid = os.fork()
    if pid != 0: # pere
        _pid, status = os.waitpid(pid, 0)
        # _pid == pid
        # ou bien
        # pid , status = os.waitpid(-1, 0) si on n'avait pas deja le pid
        if os.WIFEXITED(status):
            exit_code = os.WEXITSTATUS(status)
            print(f"child {pid} terminated normally with exit status={exit_code}")
        else:
            print("child {} terminated abnormally".format(pid))
    else: # fils
        sys.exit(100 + i)

sys.exit(0)
