from sys import stdin
from collections import defaultdict
from functions import *

tp = defaultdict(int)
players = 0

for buf in read_data(stdin):
    for i in range(len(buf)):
        for j in range(i):
        	for k in range(j):
        		tp[tuple(sorted([buf[i], buf[j], buf[k]]))] += 1
        if players <= buf[i]:
            players = buf[i] + 1

for i in range(players):
	for j in range(i+1, players):
		for k in range(j+1, players):
			print tp[(i, j, k)],
		print
