from sys import stdin

def byTwo(arr):
    while arr:
        yield arr[0] + arr[1]
        arr = arr[2:]

buf = None
for line in stdin:
    tpc = map(int, line.strip().split())
    if buf is None:
        buf = byTwo(tpc)
        continue
    for p, q in zip(byTwo(tpc), buf):
        print p+q,
    print
    buf = None
