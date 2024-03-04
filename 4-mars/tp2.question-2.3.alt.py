# autre solution sans try...except mais en utilisant 
# l'option WNOHANG pour waitpid
# on évite une erreur s'il n'y a plus de fils à attendre
# (dans ce cas waitpid renvoie (0,0) )
# cf: https://docs.python.org/3/library/os.html#os.waitpid


import os, signal, sys, time
NB_CHILDREN = 10


def CHLD_handler(signal, ignore):
    """Traitant de l'interruption SIGCHLD"""
    global nb_waits
    (pid, status) = os.waitpid(-1, os.WNOHANG)
    if pid == 0 : return
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
    while os.waitpid(-1, os.WNOHANG) != (0,0):
        pass
    ## fin collecte des zombies

    while not 'saisie' in globals():
        try:
            saisie = input("**père** tapez quelque chose... ")
        except: # La réception d'un signal provoque l'interruption de la saisie
            pass
    print("**père** Terminé !")
    sys.exit(0)