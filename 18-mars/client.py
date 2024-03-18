# client.py
import os
MAXLINE = 1000

# question 2.2.2: faire de ce fichier un programme autonome et le lancer
# avec `python3 client.py`

def client(readfd, writefd):
    nomfic = input("entrez un nom de fichier : ")
    os.write(
        writefd, nomfic.encode("utf-8")
    )  # envoyer nom fichier sur tube vers serveur
    buff = os.read(readfd, MAXLINE)  # lire contenu du fichier sur tube depuis serveur
    while len(buff) > 0:
        os.write(1, buff)  # écrire contenu du tube sur la sortie standard
        buff = os.read(readfd, MAXLINE)

if __name__ == "__main__":
    # partie qui fait de ce module un programme autonome
    # on suppose que `/tmp/tube1` et `/tmp/tube2` ont été créés
    wfd = os.open("/tmp/tube1", os.O_WRONLY)
    rfd = os.open("/tmp/tube2", os.O_RDONLY)
    client(rfd, wfd)