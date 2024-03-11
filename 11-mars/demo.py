# idee: observer qu'un fichier ouvert permet de pointer vers un inoeud
# meme si la ref dans l'arborescence vers ce inoeud est effacée.

# 1. je crée toto.txt avec "hello" dedans
# 2. je lance ce programme, je le suspend
# 3. j'efface toto.txt
# 4. je reprends ce programme

import os, time

fd = os.open("toto.txt", os.O_RDONLY)
time.sleep(10)
print(os.read(fd, 100))
