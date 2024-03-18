import os, sys
MAXLINE = 1000

def server(readfd, writefd):
    global MAXLINE
    buff = os.read(readfd, MAXLINE)
    try:
        fd = os.open(buff, os.O_RDONLY)
    except:
        os.write(writefd, b"error: can't open " + buff + b"\n")
    else:
        # ouverture réussie
        buff = os.read(fd, MAXLINE)
        while len(buff) > 0:
            os.write(writefd, buff)
            buff = os.read(fd, MAXLINE)
        os.close(fd)

if __name__ == "__main__":
    # partie qui fait de ce module un programme autonome
    # on suppose que `/tmp/tube1` et `/tmp/tube2` ont été créés
    rfd = os.open("/tmp/tube1", os.O_RDONLY)
    wfd = os.open("/tmp/tube2", os.O_WRONLY)
    server(rfd, wfd)