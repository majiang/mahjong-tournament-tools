from sys import stdin
buf = []
for line in stdin:
    buf.append(map(int, line.strip().split()))
    if len(buf) != 4:
        continue
    print ' '.join(str(sum(buf[i][j] for i in range(4))) for j in range(len(buf[0])))
    buf = []
