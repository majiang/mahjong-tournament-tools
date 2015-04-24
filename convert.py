from functions import *
from sys import stdin

buf = read_all(stdin)
while not buf[len(buf)-1]:
    buf = buf[:-1]

tables = (max(max(p) for p in buf) + 1) // 4
rounds = len(buf) // tables
players = [[] for i in range(tables * 4)]

for round in range(rounds):
    for t, table in enumerate(buf[:tables]):
        for player in table:
            players[player].append(t)
    buf = buf[tables:]

write_all(players)
