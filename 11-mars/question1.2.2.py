# qu'affiche ce programme?

import os, sys
fd1 = os.open("toto.txt", os.O_RDONLY)
fd2 = os.open("toto.txt", os.O_RDONLY)
_bytes_sequence = os.read(fd1, 2)  # séquence d'octets
bytes_sequence = os.read(fd2, 6)
os.close(fd1)
os.close(fd2)
print(bytes_sequence)
print(bytes_sequence.decode("utf-8"))
print(bytes_sequence.decode("latin-1"))
sys.exit(0)
