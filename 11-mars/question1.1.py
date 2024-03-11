# Qu'affiche le programme suivant?



import os, sys

# fd: file descriptor, descripteur de fichier
# un entier qui correspond à l'indice dans la table des descripteurs de fichiers
# qui contient le pointeur vers le fichier ouvert par le open qui renvoie fd
# c'est le premier emplacement libre de la table des descripteurs de fichiers qui est choisi

fd1 = os.open("toto.txt", os.O_RDWR)
print(fd1)
os.close(fd1) # ou ici, de maniere equivalente, os.close(3)
fd2 = os.open("titi.txt", os.O_RDONLY)
print(fd2)
fd3 = os.open("titi.txt", os.O_RDONLY)
print(fd3)
os.close(fd2)
os.close(fd3)
sys.exit(0)