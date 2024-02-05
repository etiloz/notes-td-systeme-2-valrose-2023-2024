# 1. Modifier ce programme pour qu’il affiche les numéro des 
# processus dans l’ordre dans lequel ils ont été créés.
# solution "super triche": on endort les fils de plus en plus longtemps
import errno, os, sys, time
nbChildren = 20
for i in range(nbChildren):
    pid = os.fork()
    if pid == 0: # child
        time.sleep(i) # dort i secondes, puis termine par un exit
        sys.exit(100 + i)

for _ in range(nbChildren):
    pid, status = os.waitpid(-1, 0)
    if os.WIFEXITED(status):
        exit_code = os.WEXITSTATUS(status)
        print(f"child {pid} terminated normally with exit status={exit_code}")
    else:
        print("child {} terminated abnormally".format(pid))
print("No more children left. Bye", file=sys.stderr)
