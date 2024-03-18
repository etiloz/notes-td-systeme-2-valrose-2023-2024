# exercice:
# écrire un programme qui simule l'exécution de la 
# commande shell `ls -l | grep mars`

# le processus parent cree deux enfants
# le premier execute `ls -l` et le second `grep mars`
# on a redirigé au préalable la sortie standard du premier
# processus vers un tube anonyme, et la sortie standard du
# second processus vers le tube anonyme

# commandes utiles:
# os.pipe() : crée un tube anonyme
# os.fork() : crée un processus enfant
# os.dup2(fd1, fd2) : duplique fd1 sur fd2 (utile pour faire une redirection)
# os.close(fd) : ferme le descripteur fd
# os.exevp(executable, [executable, arg1, arg2, ...]) : remplace le processus courant par un autre
# os.wait() : attend la terminaison d'un processus enfant

import os
(fd_read, fd_write) = os.pipe()
pid_child1 = os.fork()

if pid_child1 == 0:
    # la redirection de la sortie standard (1) vers le tube
    os.close(fd_read) # ferme le descripteur inutile (bonne pratique)
    os.dup2(fd_write, 1) # equivalent à # `os.close(1); os.dup(fd_write)` 
    print("je suis sur mars") # -> va dans le tube
    print("je suis sur terre") # -> va dans le tube, mais ne sera pas affiché par grep
    os.execvp("ls", ["ls", "-l"]) # fonction qui ne retourne pas, child1 devient `ls -l`
    # non accessible
    assert(false)

os.close(fd_write) # ferme le descripteur inutile, evite que fils2 et pere soient consideres comme ecrivains dans le tube
pid_child2 = os.fork()
if pid_child2 == 0:
    # la redirection de l'entree standard (0) vers le tube
    os.dup2(fd_read, 0) # equivalent à # `os.close(0); os.dup(fd_read)`
    os.execvp("grep", ["grep", "mars"]) # fonction qui ne retourne pas, child2 devient `grep mars`
    # non accessible
    assert(false)

os.waitpid(pid_child1, 0) # attend la terminaison du premier processus
os.waitpid(pid_child2, 0) # attend la terminaison du second processus
print("fini!")