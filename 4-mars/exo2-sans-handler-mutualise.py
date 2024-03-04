import os, sys, signal, time

def handler_pere(_sig, _ignore):
    global pid_fils
    print("père: signal reçu")
    os.kill(pid_fils, signal.SIGUSR1)

signal_recu = False

def handler_fils(_sig, _ignore):
    global signal_recu
    print("fils: signal reçu")
    signal_recu = True
    sys.exit(0)


signal.signal(signal.SIGUSR1, handler_pere)
pid_fils = os.fork()
if pid_fils == 0:
    #fils
    signal.signal(signal.SIGUSR1, handler_fils)
    pid_pere = os.getppid()
    os.kill(pid_pere, signal.SIGUSR1)
    # boucle attente active
    while not signal_recu:
        pass
    sys.exit(0)
# père
os.wait()
sys.exit(0)
