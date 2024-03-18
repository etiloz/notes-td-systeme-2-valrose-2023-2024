## demonstration de os.pipe

import os, time

# creation du tube anonyme et ouverture des descripteurs
(fd_read, fd_write) = os.pipe()
# equivalent à 
# os.mkfifo("tmp/unnommed_tube") 
# fd_read = open("tmp/unnommed_tube", O_RDONLY) 
# fd_write = open("tmp/unnommed_tube", O_WRONLY)

os.write(fd_write, b"hello world\n")
s = os.read(fd_read, 4) # lit 4 octets
print(s)
time.sleep(1)
s = os.read(fd_read, 12) # lit 12 octets
print(s)
