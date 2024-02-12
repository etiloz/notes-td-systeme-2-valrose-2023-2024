import os
argv = ["ls", "-lt", "/"]
os.execv("/bin/ls", argv)

# le nom du fichier est en argv[0] par convention
# mais ls s'en fiche, donc ceci marche aussi
argv = ["toto", "-lt", "/"]
os.execv("/bin/ls", argv)

# en général après os.execv il ne se passe rien... sauf si le fichier n'existe
# pas, dans ce cas une exception est levee
try:
    os.execv("/binoo/ls", argv)
except:
    pass
print("le fichier `/binoo/ls` n'existe pas")