# ecrivain dans le tube
# equivalent à `cat > tube``
import os

fd_tube = os.open("tube", os.O_WRONLY)
print("communication établie")
while True:
    c = os.read(0, 1) # lit un octet sur l'entree standard
    if c == b'': break
    os.write(fd_tube, c) # le recopie dans tube