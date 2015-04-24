from sys import stdin
for line in stdin:
    buf = map(int, line.strip().split())
    print ' '.join(str(sum(buf[(4*i):(4*(i+1))])) for i in range(len(buf) / 4))
