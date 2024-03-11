# qu'affiche ce programme?

import os, sys
fd = os.open("toto.txt", os.O_RDONLY)
pid = os.fork()
if pid == 0:
    bytes = os.read(fd, 1000)   ## EN C: `char bytes[1000]; int n = read(fd, 1000, &bytes);
    print(f"[fils] {c=}")
    sys.exit(0)
os.wait()
c = os.read(fd, 1)
print(f"[père] {c=}")
sys.exit(0)