from sys import stdin

for line in stdin:
    if line.strip():
        for elem in line.strip().split():
            print elem
    else:
        print
