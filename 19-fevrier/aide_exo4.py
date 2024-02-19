# aide pour faire l'exo 4

import signal

# on veut reprogrammer os.wait

def traitant(_signum, _ignore):
    global sigchld_received
    sigchld_received = True

def os_wait():
    global sigchld_received
    sigchld_received = False
    signal.signal(signal.SIGCHLD, traitant)
    while not sigchld_received:
        signal.pause()

