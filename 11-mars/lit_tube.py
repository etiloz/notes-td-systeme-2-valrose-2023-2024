# lecteur dans le tube
# equivalent à `cat < tube``

# terminaison: fermer l'entree standard avec ^D
import os

fd_tube = os.open("tube", os.O_RDONLY)
print("communication établie")
while True:
    c = os.read(fd_tube, 1) # lit un octet sur l'entree standard
    if c == b'': break
    os.write(1, c) # le recopie dans la sortie standard