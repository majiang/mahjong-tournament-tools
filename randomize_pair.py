from sys import stdin
from random import shuffle
buff = []
buf = None
for line in map(lambda x: x.strip(), stdin):
    if buf is None:
        buf = [line]
    else:
        buff.append(buf + [line])
        buf = None

shuffle(buff)
for buf in buff:
    shuffle(buf)
    for line in buf:
        print line
