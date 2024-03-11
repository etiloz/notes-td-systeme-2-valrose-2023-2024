# qu'affiche ce programme?

import os, sys
fd1 = os.open("toto.txt", os.O_RDONLY)
fd2 = os.open("toto.txt", os.O_RDONLY)
c = os.read(fd2, 1)
os.dup2(fd2, fd1)
c = os.read(fd1, 1)
os.close(fd1)
os.close(fd2)
print(c)
sys.exit(0)