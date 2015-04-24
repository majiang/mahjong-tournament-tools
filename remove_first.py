from sys import stdin

for line in stdin:
	b = line.strip().split()[1:]
	if len(b):
		print ' '.join(b)
