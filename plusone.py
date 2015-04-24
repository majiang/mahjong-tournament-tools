from sys import stdin
for line in stdin:
    print ' '.join(map(lambda x: str(1+int(x)), line.strip().split()))
