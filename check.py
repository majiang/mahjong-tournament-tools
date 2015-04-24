from sys import stdin
from collections import defaultdict
from functions import *

tp = defaultdict(int)
players = 0

for buf in read_data(stdin):
    for i in range(len(buf)):
        for j in range(i):
            tp[(buf[i], buf[j])] += 1
            tp[(buf[j], buf[i])] += 1
        if players <= buf[i]:
            players = buf[i] + 1

write_all((tp[(i, j)] for j in range(players)) for i in range(players))
