from sys import stdin
from functions import *

DEBUG = False

players = read_all(stdin)
rounds = len(players[0])
tables = len(players) // 4

table_players = [[[] for j in range(tables)] for i in range(rounds)]
for i in range(len(players)):
    for round in range(rounds):
    	if DEBUG:
    		print '[%d][%d]' % (len(table_players), round)
    		print '[%d][%d]' % (len(players[i]), round)
    		print '[%d][%d]' % (len(table_players[round]), players[i][round])
        table_players[round][players[i][round]].append(i)

for round in table_players:
    write_all(round)
    print
