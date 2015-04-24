def read_data(f):
    for line in f:
        c = map(int, line.strip().split())
        if c:
            yield c

def read_all(f):
    return list(read_data(f))

def write_all(b):
    for line in b:
        print ' '.join(map(str, line))
