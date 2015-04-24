from sys import stdin

seats = ['ESWN', 'SENW', 'WNSE', 'NWES']

c = 0
for line in stdin:
    print ' '.join(p+q for p, q in zip(line.strip().split(), seats[c & 3]))
    c += 1
