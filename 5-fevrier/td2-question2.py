import os, sys
print("Hello")
toto = os.fork()
#print("ici : {}".format(os.getpid()))
print("ici : {}".format(toto))
if toto != 0:
    pid_wait, status = os.waitpid(-1, 0)
    if os.WIFEXITED(status):
        print("là : {}".format(os.WEXITSTATUS(status)))
    print("Bye")
    sys.exit(2)
sys.exit(0) # optionnel, implicite en fin de programme