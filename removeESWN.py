from sys import stdin
for line in stdin:
    print ' '.join(map(lambda x: x[0:-1], line.strip().split()))
