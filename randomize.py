from sys import stdin
from functions import *

players = read_all(stdin)
tables = max(map(max, players)) + 1
rounds = len(players[0])

from random import sample
new_tables = list(sample(range(tables), tables) for i in range(rounds))

write_all([new_tables[round][player[round]] for round in range(rounds)] for player in players)
