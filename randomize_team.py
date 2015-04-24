from sys import stdin
from random import shuffle
buff = []
buf = []
c = 0
for line in map(lambda x: x.strip(), stdin):
    if not buf:
        buf = [line]
    else:
        buf.append(line)
    c += 1
    if c % 4 == 0:
        buff.append(buf)
        buf = []

shuffle(buff)
for buf in buff:
    shuffle(buf)
    for line in buf:
        print line
