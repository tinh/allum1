#! /usr/bin/env python3.3

import sys

def gen_allum(nb_rang = 4):
	nb_allum = 1
	allums = list(range(nb_rang))
	for i in allums:
		allums[i] = nb_allum
		nb_allum += 2
	return allums

def print_allum(allums):
	i = 0
	while i < len(allums):
		print(' ' * (len(allums) - (i + 1)), end = ' ')
		print('|' * allums[i])
		i += 1

def usage():
	print(sys.argv[0], '[1:player vs computer|2:player vs player] [nb_rangs (by default 4)]')

def main():
	if len(sys.argv) < 2:
		usage()
	else:
		if len(sys.argv) > 2:
			allums = gen_allum(int(sys.argv[2]))
		else:
			allums = gen_allum()
		print_allum(allums)

if __name__ == "__main__":
	main()