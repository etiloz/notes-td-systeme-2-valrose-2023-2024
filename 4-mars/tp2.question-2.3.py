import os, signal, sys, time
NB_CHILDREN = 10


def CHLD_handler(signal, ignore):
    """Traitant de l'interruption SIGCHLD"""
    global nb_waits
    pid, status = os.wait()
    if os.WIFEXITED(status):
        print("**père** child %d terminated normally with exit status=%d" %\
            (pid, os.WEXITSTATUS(status)))
    else:
        print("**père** child %d terminated abnormally" % pid)

# Programme principal
if __name__ == '__main__':
    signal.signal(signal.SIGCHLD, CHLD_handler) # Installe le traitant
    for i in range(NB_CHILDREN): # Création des fils
        pid = os.fork()
        if pid == 0:
            print("------> fils (pid = %d). Je me termine." % os.getpid())
            sys.exit(1 + i)
        else:
            print("**père** fils créé, pid = %d" % pid)


    ## collecte des zombies
    try:
        while True:
            os.wait()
    except:
        pass
    ## fin collecte des zombies

    while not 'saisie' in globals():
        try:
            saisie = input("**père** tapez quelque chose... ")
        except: # La réception d'un signal provoque l'interruption de la saisie
            pass
    print("**père** Terminé !")
    sys.exit(0)