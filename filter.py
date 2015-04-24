from sys import stdin
c = 0
for line in stdin:
    c += 1
    print line.strip()
    if c == 5:
        break
