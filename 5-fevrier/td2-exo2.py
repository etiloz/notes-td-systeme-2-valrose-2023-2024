# 1. Écrire un programme Python qui affiche son PID, puis crée un fils. 
# Le père affiche son PID, puis affiche un message signalant que son fils 
# est mort lorsque c’est bien le cas. 
# Le fils affiche son PID, s’endort 5 secondes puis se termine.


import os, sys, time
my_pid = os.getpid()
print(f"{my_pid=}")
toto = os.fork()
if toto == 0:
    # je suis le fils
    my_pid2 = os.getpid()
    print(f"{my_pid2=}")
    time.sleep(5)
    sys.exit(0)
else:
    # je suis le père
    print(f"{my_pid=}")
    pid_du_fils = toto
    os.waitpid(pid_du_fils, 0)
    # ou bien, comme il y a un seul fils
    # os.waitpid(-1, 0)
    # ou encre
    # os.wait()
    print("mon fils est mort")
    sys.exit(0)