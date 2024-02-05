# 1. Modifier ce programme pour qu’il affiche les numéro des 
# processus dans l’ordre dans lequel ils ont été créés.

import errno, os, sys
nbChildren = 20
pids = [] # la liste des fils créés
for i in range(nbChildren):
    pid = os.fork()
    if pid == 0: # child
        sys.exit(100 + i)
    else: # father: update `pids`
        pids.append(pid) # add the pid of the new child to the end of `pids`
#        print(f"fils {pid} créé, {pids=}")

for pid in pids:
    _pid, status = os.waitpid(pid, 0)
    # _pid == pid
    if os.WIFEXITED(status):
        exit_code = os.WEXITSTATUS(status)
        print(f"child {pid} terminated normally with exit status={exit_code}")
    else:
        print("child {} terminated abnormally".format(pid))
print("No more children left. Bye", file=sys.stderr)

sys.exit(0)
