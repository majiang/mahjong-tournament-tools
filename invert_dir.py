from sys import stdin
from functions import *

players = filter(None, map(lambda line: line.strip().split(), stdin))
rounds = len(players[0])
tables = len(players) // 4

def fromNDtoTuple(p):
    if p[-1:] == 'E':
        return (int(p[:-1]), 0)
    if p[-1:] == 'S':
        return (int(p[:-1]), 1)
    if p[-1:] == 'W':
        return (int(p[:-1]), 2)
    if p[-1:] == 'N':
        return (int(p[:-1]), 3)
    return 4

table_players = [[[None for k in range(4)] for j in range(tables)] for i in range(rounds)]
for i in range(len(players)):
    for round in range(rounds):
        table, seat = fromNDtoTuple(players[i][round])
        #print 'debug: table, seat = ', table, seat
        table_players[round][table-1][seat] = i+1

for round in table_players:
    write_all(round)
    print
